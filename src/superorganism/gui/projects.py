import superorganism.gui.view
import urwid
import zope.component
import zope.schema


class EditProject(superorganism.gui.view.BaseView):

    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    fields = superorganism.gui.interfaces.INewProjectForm

    def run(self):
        while 1:
            size = self.screen.get_cols_rows()
            self.render()
            keys = self.screen.get_input()
            widget, pos = self.widget.get_focus()

            for key in keys:
                self.widget.set_statusmsg('Key: %s' % key)
                if superorganism.gui.interfaces.IButton.providedBy(widget):
                    if (widget.get_label().startswith('Save') and key == 'enter'):
                        return zope.component.getMultiAdapter(
                            (self.context.__parent__, self.screen),
                            superorganism.gui.interfaces.ITerminalView).run()
                self.widget.keypress(size, key)

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
