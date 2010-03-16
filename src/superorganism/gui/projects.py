import superorganism.gui.view
import transaction
import urwid
import zope.component
import zope.component.interfaces
import zope.component.event
import zope.schema
import zope.event


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

            adapter = zope.component.getMultiAdapter(
                (self.screen, self), superorganism.gui.interfaces.IKeyDispatcher)
            adapter.dispatch_key_events()



@zope.component.adapter(superorganism.gui.interfaces.ICharKeyPressEvent)
def handle_keypress(event):
    raise ValueError(superorganism.gui.interfaces.IWidget.providedBy(event.widget))
