import superorganism.gui.view
import zope.schema
import urwid


class NewProjectForm(superorganism.gui.view.BaseView):

    zope.interface.implements(superorganism.gui.interfaces.INewProjectForm)
    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    def update_widgets(self):
        fields = superorganism.gui.interfaces.INewProjectForm
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(fields):
            widgets.append(widgetFactory(self.context, field))
        walker = urwid.SimpleListWalker(widgets)
        self.pile = urwid.ListBox(walker)

    def render(self):
        self.update_widgets()
        size = self.screen.get_cols_rows()
        canvas = self.pile.render(size, focus=True)
        self.screen.draw_screen(size, canvas)


def widgetFactory(context, field):
    """Currently simple widget factory to create urwid widgets depending
       to zope.schema.
    """
    # XXX currently it doesn't really matter which urwid widget we
    # create according to the schema. We expect text input. We have to
    # create more sophisticated widget and fields for validation tho.
    return urwid.Edit(field.title, field.get(context))
