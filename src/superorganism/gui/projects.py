import superorganism.gui.view
import superorganism.gui.interfaces
import urwid
import zope.component
import zope.schema


class EditProject(superorganism.gui.view.BaseView):

    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    fields = superorganism.gui.interfaces.INewProjectForm

    def contents(self):
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(self.fields):
            widgets.append(
                zope.component.getMultiAdapter(
                    (field, self), superorganism.gui.interfaces.IFormWidget))
        save = superorganism.gui.widgets.DialogButton("Save")
        urwid.connect_signal(save, 'click', save_clicked, self)
        widgets.append(
            urwid.GridFlow(
                [save,
                 superorganism.gui.widgets.DialogButton("Cancel")],
                10, 3, 1, 'center'
            ))
        return urwid.SimpleListWalker(widgets)

def save_clicked(button, view):
    app = view.context.__parent__
    return zope.component.getMultiAdapter(
        (app, view.screen),
        superorganism.gui.interfaces.ITerminalView)
