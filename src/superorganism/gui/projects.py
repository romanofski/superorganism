import superorganism.gui.view
import superorganism.gui.interfaces
import superorganism.gui.app
import urwid
import zope.component
import zope.schema


class BaseForm(superorganism.gui.view.BaseView):

    fields = None
    layout = None
    formwidgets = None
    ignoreContext = False

    def extractData(self):
        info = {}
        for widget in self.formwidgets:
            info[widget.__name__] = widget.value
        return info


class AddProject(BaseForm):

    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    fields = superorganism.gui.interfaces.IProjectForm
    layout = "projectdialog"
    ignoreContext = True

    def save(self):
        data = self.extractData()
        project = zope.component.getUtility(
            zope.component.interfaces.IFactory,
            u'superorganism.Project')(
                'project', data['title'], data['description'])
        name = 'project%s' % len(self.context.keys())
        self.context[name] = project
        self.nextview()

    def nextview(self):
        return zope.component.getMultiAdapter(
            (self.context, self.screen)).run()


class EditProject(BaseForm):

    zope.component.adapts(
        superorganism.interfaces.IProject,
        superorganism.gui.interfaces.IScreen)

    fields = superorganism.gui.interfaces.IProjectForm
    layout = "projectdialog"

    def save(self):
        data = self.extractData()
        context = self.context
        for name, field in zope.schema.getFieldsInOrder(self.fields):
            field.set(context, data[name])


class ProjectDialog(superorganism.gui.app.ApplicationLayout):

    def create_body(self):
        widgets = []
        for name, field in zope.schema.getFieldsInOrder(self.view.fields):
            widget = zope.component.getMultiAdapter(
                (field, self.view.screen),
                superorganism.gui.interfaces.IFormFieldWidget)
            if self.view.ignoreContext == False:
                widget.context = self.view.context
                zope.interface.alsoProvides(
                    widget, superorganism.gui.interfaces.IContextAware)
            widget.ignoreContext = self.view.ignoreContext
            widget.update()
            widgets.append(widget)
        self.view.formwidgets = widgets
        return urwid.SimpleListWalker(self.view.formwidgets)
