import ZODB.DB
import ZODB.FileStorage
import colony.bug
import colony.gui.interfaces
import urwid
import zope.interface


class Application(object):

    zope.interface.implements(colony.gui.interfaces.IApplication)

    def __init__(self, tui, config):
        self.tui = tui
        self.config = config
        # ZConfig
        storage = ZODB.FileStorage.FileStorage(config['database'])
        self._conn = ZODB.DB(storage).open()
        self._root = self._conn.root()
        self.tui.register_palette_entry('status', 'white', 'dark blue', None)
        self.tui.register_palette_entry('bg', 'dark blue', 'dark cyan', None)

    def run(self):
        self.size = self.tui.get_cols_rows()
        self.set_status('0 Bugs')

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
                    self._conn.close()
                    return
                else:
                    self.frame.keypress(self.size, key)

                self.redisplay()

    def redisplay(self):
        canvas = self.frame.render(self.size, focus=True)
        self.tui.draw_screen(self.size, canvas)

    def set_status(self, text, align='left'):
        self.status = urwid.Text(text, align=align)

    def list_bugs(self):
        # read ZODB
        root = self._conn.root()
        result = []
        for bug in root.values():
            result.append(urwid.Text(u'%s %s %s' % (bug.id,
                                                    bug.reported,
                                                    bug.title)))
        return result
