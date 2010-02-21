import superorganism.gui.interfaces
import superorganism.gui.view
import superorganism.interfaces
import superorganism.project
import transaction
import urwid
import zope.interface


class Dashboard(superorganism.gui.view.View):

    zope.interface.implements(superorganism.gui.interfaces.IDashboard)
    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    def run(self):
        self.render()

        while 1:
            keys = self.screen.get_input()

            for key in keys:
                if key == 'window resize':
                    self.size = self.screen.get_cols_rows()
                elif key == 'q':
                    transaction.commit()
                    return
                else:
                    self.frame.keypress(self.size, key)

    def register_colors(self):
        for name, fg, bg, dummy in self.context.colors:
            self.screen.register_palette_entry(name, fg.strip(), bg.strip(), None)

    def render(self):
        self.size = self.screen.get_cols_rows()
        projects = zope.component.getUtilitiesFor(superorganism.interfaces.IProject)
        self.set_status('%s Project(s)' % len(list(projects)))

        self.helpbar = urwid.Text(u'Topbar')
        self.lines = self.list_bugs()
        self.listbox = urwid.ListBox(self.lines)

        self.top = urwid.Pile([urwid.AttrMap(self.helpbar, 'helpbar')])
        self.frame = urwid.Frame(self.listbox,
                                 header=urwid.AttrMap(self.helpbar,
                                                      'helpbar'),
                                 footer=urwid.AttrMap(self.status,
                                                      'statusbar'))
        self.frame.set_focus('footer')
        canvas = self.frame.render(self.size, focus=True)
        self.screen.draw_screen(self.size, canvas)
        transaction.commit()

    def set_status(self, text, align='left'):
        self.status = urwid.Text(text, align=align)

    def list_bugs(self):
        # read ZODB
        root = zope.component.getUtility(superorganism.interfaces.IDatabase).root
        result = []
        for bug in root.values():
            result.append(urwid.Text(u'%s %s %s' % (bug.id,
                                                    bug.reported,
                                                    bug.title)))
        return result
