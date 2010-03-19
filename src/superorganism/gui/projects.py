import superorganism.gui.view
import urwid
import zope.component
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
        button = urwid.Button('Save')
        widgets.append(button)
        walker = urwid.SimpleListWalker(widgets)
        self.widget = urwid.ListBox(walker)

    def run(self):
        self.render()

        while 1:
            size = self.screen.get_cols_rows()
            canvas = self.widget.render(size, focus=True)
            self.screen.draw_screen(size, canvas)
            keys = self.screen.get_input()
            widget, pos = self.widget.get_focus()

            for key in keys:
                if (hasattr(widget, 'get_label') and\
                    widget.get_label().startswith('Save') and key == 'q'):
                    return zope.component.getMultiAdapter(
                        (self.context.__parent__, self.screen),
                        name='dashboard').run()

                self.widget.keypress(size, key)
