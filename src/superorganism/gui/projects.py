import superorganism.gui.view
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
        widgets.append(
            urwid.GridFlow(
                [superorganism.gui.widgets.DialogButton("Save"),
                 superorganism.gui.widgets.DialogButton("Cancel")],
                10, 3, 1, 'center'
            ))
        return urwid.SimpleListWalker(widgets)
