import superorganism.gui.view
import superorganism.gui.interfaces
import superorganism.gui.app
import urwid
import zope.component
import zope.schema


class EditProject(superorganism.gui.view.BaseView):

    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    fields = superorganism.gui.interfaces.INewProjectForm
    layout = "projectdialog"


class ProjectDialog(superorganism.gui.app.ApplicationLayout):

    def create_body(self):
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(self.view.fields):
            widget = zope.component.getMultiAdapter(
                (field, self.view.screen),
                superorganism.gui.interfaces.IFormFieldWidget)
            widgets.append(widget)
        save = superorganism.gui.widgets.DialogButton("Save")
        widgets.append(
            urwid.GridFlow(
                [save,
                 superorganism.gui.widgets.DialogButton("Cancel")],
                10, 3, 1, 'center'
            ))
        return urwid.SimpleListWalker(widgets)
