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
                    self.frame.keypress(self.size, key)

    def register_colors(self):
        for name, fg, bg, dummy in self.context.colors:
            self.screen.register_palette_entry(name, fg.strip(), bg.strip(), None)

    def render(self):
        self.size = self.screen.get_cols_rows()
        self.status = urwid.Text(self.statusmsg, align='left')

        self.helpbar = urwid.Text(u'Topbar')
        self.lines = self.list_bugs()
        self.listbox = urwid.ListBox(self.lines)

        self.top = urwid.Pile([urwid.AttrMap(self.helpbar, 'helpbar')])
        self.frame = urwid.Frame(self.listbox,
                                 header=urwid.AttrMap(self.helpbar, 'helpbar'),
                                 footer=urwid.AttrMap(self.status, 'statusbar'))
        self.frame.set_focus('footer')
        canvas = self.frame.render(self.size, focus=True)
        self.screen.draw_screen(self.size, canvas)

    def create_project(self):
        transaction.commit()
        transaction.begin()
        project = zope.component.getUtility(
            zope.component.interfaces.IFactory,
            u'superorganism.Project')(
                'project', '<Title>', '<Description>')
        name = 'project%s' % len(self.context.keys())
        self.context[name] = project
        project.__parent__ = self.context
        return zope.component.getMultiAdapter(
            (project, self.screen), name='newproject').render()

    def list_bugs(self):
        # read ZODB
        root = zope.component.getUtility(superorganism.interfaces.IDatabase).root
        result = []
        for bug in root.values():
            result.append(urwid.Text(u'%s %s %s' % (bug.id,
                                                    bug.reported,
                                                    bug.title)))
        return result



class CharKeyPressed(object):

    zope.interface.implements(superorganism.gui.interfaces.ICharKeyPressEvent)

    def __init__(self, key):
        self.key = key


class FunctionKeyPressed(CharKeyPressed):

    zope.interface.implements(superorganism.gui.interfaces.IFunctionKeyPressEvent)


class KeyDispatcher(object):

    zope.interface.implements(superorganism.gui.interfaces.IKeyDispatcher)
    zope.component.adapts(superorganism.gui.interfaces.IScreen,
                          superorganism.gui.interfaces.ITerminalView)

    def __init__(self, screen, view):
        self.screen = screen
        self.view = view

    def dispatch_key_events(self):
        keys = self.screen.get_input()
        for key in self.screen.get_input():
            if self.is_valid_char(key):
                zope.event.notify(
                    superorganism.gui.app.CharKeyPressed(key))
            else:
                zope.event.notify(
                    superorganism.gui.app.FunctionKeyPressed(key))


    def is_valid_char(self, key):
        return urwid.util.is_wide_char(key,0) or (len(key)==1 and ord(key) >= 32)
