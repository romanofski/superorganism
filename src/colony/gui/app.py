import ConfigParser
import ZODB.DB
import ZODB.FileStorage
import colony.gui.interfaces
import colony.interfaces
import colony.project
import os.path
import transaction
import urwid
import zope.interface


class Application(object):

    zope.interface.implements(colony.gui.interfaces.IApplication)

    def __init__(self, tui, config):
        self.tui = tui
        self.config = config
        self.configure()

    def configure(self):
        confdir = self.config['configdir']
        guiconf = ConfigParser.SafeConfigParser()
        guiconf.read(os.path.join(confdir, 'gui.cfg'))
        for name, val in guiconf.items('colors'):
            fg, bg = val.split(',')
            self.tui.register_palette_entry(name, fg.strip(), bg.strip(), None)
        # register projects
        _projects = guiconf.get('app', 'projects')
        for proj in _projects.split('\s'):
            project = colony.project.Project(
                guiconf.get(proj, 'title'),
                guiconf.get(proj, 'description'))
            zope.component.provideUtility(project,
                                          colony.interfaces.IProject)

    def run(self):
        self.size = self.tui.get_cols_rows()
        projects = zope.component.getUtilitiesFor(colony.interfaces.IProject)
        self.set_status('%s Project(s)' % len(list(projects)))

        self.lines = self.list_bugs()
        self.listbox = urwid.ListBox(self.lines)
        self.input = urwid.Edit()

        self.bframe = urwid.Pile([urwid.AttrMap(self.status, 'status'), self.input])
        self.frame = urwid.Frame(self.listbox, footer=self.bframe)
        self.frame.set_focus('footer')

        self.redisplay()

        while 1:
            keys = self.tui.get_input()

            for key in keys:
                if key == 'window resize':
                    self.size = self.tui.get_cols_rows()
                elif key in ('up', 'down', 'page up', 'page down'):
                    self.listbox.keypress(self.size, key)
                elif key == 'q':
                    transaction.commit()
                    return
                else:
                    self.frame.keypress(self.size, key)

                self.redisplay()

    def redisplay(self):
        transaction.commit()
        canvas = self.frame.render(self.size, focus=True)
        self.tui.draw_screen(self.size, canvas)

    def set_status(self, text, align='left'):
        self.status = urwid.Text(text, align=align)

    def list_bugs(self):
        # read ZODB
        root = zope.component.getUtility(colony.interfaces.IDatabase).root
        result = []
        for bug in root.values():
            result.append(urwid.Text(u'%s %s %s' % (bug.id,
                                                    bug.reported,
                                                    bug.title)))
        return result
