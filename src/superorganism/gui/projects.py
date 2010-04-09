import superorganism.gui.view
import superorganism.gui.interfaces
import superorganism.gui.app
import transaction
import urwid
import zope.component
import zope.schema


class Projects(superorganism.gui.view.BaseView):

    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    def add_project(self):
        return zope.component.getMultiAdapter(
            (self.context, self.screen), name='addproject').run()

    def edit_project(self):
        widget, pos = self.widget.get_focus()
        # XXX we assume that the widget position equals the project in
        # the list of values
        project = self.context.values()[pos]
        return zope.component.getMultiAdapter(
            (project, self.screen), name='editproject').run()

    def delete_project(self):
        widget, pos = self.widget.get_focus()
        project = self.context.values()[pos]
        del self.context[project.__name__]
        return zope.component.getMultiAdapter(
            (self.context, self.screen),
            superorganism.gui.interfaces.ITerminalView).run()


class BaseForm(superorganism.gui.view.BaseView):

    fields = None
    layout = None
    ignoreContext = False

    def __init__(self, context, screen):
        self.formwidgets = []
        super(BaseForm, self).__init__(context, screen)


    def extractData(self):
        info = {}
        for widget in self.formwidgets:
            info[widget.__name__] = widget.extract()
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
    formwidgets = []

    def save(self):
        data = self.extractData()
        context = self.context
        for name, field in zope.schema.getFieldsInOrder(self.fields):
            field.set(context, data[name])
        self.nextview()

    def nextview(self):
        app = superorganism.interfaces.IApplication(self.context.__parent__)
        return zope.component.getMultiAdapter(
            (app, self.screen),
            superorganism.gui.interfaces.ITerminalView).run()


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
            self.view.formwidgets.append(widget)
            widgets.append(widget)
            widgets.append(urwid.Divider())
        return urwid.SimpleListWalker(widgets)
