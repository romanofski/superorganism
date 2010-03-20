import superorganism.gui.interfaces
import superorganism.gui.view
import superorganism.interfaces
import superorganism.project
import transaction
import urwid
import zope.component
import zope.component.interfaces
import zope.interface


class Dashboard(superorganism.gui.view.BaseView):

    zope.interface.implements(superorganism.gui.interfaces.IDashboard)
    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    statusmsg = u''

    # XXX Todo: that should be refactored into some sort of
    # key-dispatcher utility, which creates the views depending on the
    # keypress. Although I'm not sure if that will work out.
    def run(self):
        self.statusmsg = '%s Project(s)' % len(list(self.context.keys()))
        self.render()

        while 1:
            keys = self.screen.get_input()

            for key in keys:
                if key == 'window resize':
                    self.size = self.screen.get_cols_rows()
                elif key == 'q':
                    transaction.commit()
                    return
                elif key == 'p':
                    return self.create_project()
                elif key == 'd':
                    return zope.component.getMultiAdapter(
                        (self.context, self.screen), name='dashboard').render()
                else:
                    self.widget.keypress(self.size, key)

    def update_widgets(self):
        self.size = self.screen.get_cols_rows()
        self.status = urwid.Text(self.statusmsg, align='left')

        self.helpbar = urwid.Text(u'Topbar')
        self.lines = self.list_bugs()
        self.listbox = urwid.ListBox(self.lines)

        self.top = urwid.Pile([urwid.AttrMap(self.helpbar, 'helpbar')])
        self.widget = urwid.Frame(self.listbox,
                                 header=urwid.AttrMap(self.helpbar, 'helpbar'),
                                 footer=urwid.AttrMap(self.status, 'statusbar'))
        self.widget.set_focus('body')

    def register_colors(self):
        for name, fg, bg, dummy in self.context.colors:
            self.screen.register_palette_entry(name, fg.strip(), bg.strip(), None)

    def create_project(self):
        transaction.commit()
        project = zope.component.getUtility(
            zope.component.interfaces.IFactory,
            u'superorganism.Project')(
                'project', '<Title>', '<Description>')
        name = 'project%s' % len(self.context.keys())
        self.context[name] = project
        project.__parent__ = self.context
        return zope.component.getMultiAdapter(
            (project, self.screen), name='newproject').run()

    def list_bugs(self):
        result = []
        for bug in self.context.values():
            result.append(urwid.Text(u'%s %s' % (bug.uid, bug.title)))
        return result

