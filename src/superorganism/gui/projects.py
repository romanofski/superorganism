import superorganism.gui.view
import zope.schema
import urwid


class NewProjectForm(superorganism.gui.view.BaseView):

    zope.interface.implements(superorganism.gui.interfaces.INewProjectForm)
    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    def update_widgets(self):
        fields = superorganism.gui.interfaces.INewProjectForm
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(fields):
            input = urwid.Edit(field.title)
            widgets.append(input)
        walker = urwid.SimpleListWalker(widgets)
        self.pile = urwid.ListBox(walker)

    def render(self):
        self.update_widgets()
        size = self.screen.get_cols_rows()
        canvas = self.pile.render(size, focus=True)
        self.screen.draw_screen(size, canvas)
