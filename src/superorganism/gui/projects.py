import superorganism.gui.view
import transaction
import urwid
import zope.component
import zope.component.interfaces
import zope.schema


class NewProjectForm(superorganism.gui.view.BaseView):

    zope.interface.implements(superorganism.gui.interfaces.INewProjectForm)
    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    def update_widgets(self):
        fields = superorganism.gui.interfaces.INewProjectForm
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(fields):
            widgets.append(
                zope.component.getMultiAdapter(
                    (field, self), superorganism.gui.interfaces.IWidget))
        self.walker = urwid.SimpleListWalker(widgets)
        self.listbox = urwid.ListBox(self.walker)

    def render(self):
        self.update_widgets()
        size = self.screen.get_cols_rows()

        while 1:
            canvas = self.listbox.render(size, focus=True)
            self.screen.draw_screen(size, canvas)
            keys = self.screen.get_input()
            widget, pos = self.listbox.get_focus()

            for key in keys:
                if key == 'window resize':
                    self.size = self.screen.get_cols_rows()
                elif key == 'q':
                    transaction.abort()
                    app = superorganism.interfaces.IApplication(
                        self.context.__parent__)
                    return zope.component.getMultiAdapter(
                        (app, self.screen), name='dashboard').run()
                elif key == 'up':
                    self.listbox.keypress(size, key)
                elif key == 'down':
                    self.listbox.keypress(size, key)
                else:
                    widget, pos = self.listbox.get_focus()
                    widget.keypress((size[0],), key)


def widgetFactory(context, field):
    """Currently simple widget factory to create urwid widgets depending
       to zope.schema.
    """
    # XXX currently it doesn't really matter which urwid widget we
    # create according to the schema. We expect text input. We have to
    # create more sophisticated widget and fields for validation tho.
    return 
