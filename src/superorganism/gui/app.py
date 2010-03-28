import superorganism.gui.interfaces
import superorganism.gui.view
import superorganism.gui.widgets
import superorganism.interfaces
import superorganism.project
import transaction
import urwid
import zope.component
import zope.component.interfaces
import zope.interface


class BugList(superorganism.gui.view.BaseView):

    zope.component.adapts(
        superorganism.interfaces.IApplication,
        superorganism.gui.interfaces.IScreen)

    # XXX Todo: that should be refactored into some sort of
    # key-dispatcher utility, which creates the views depending on the
    # keypress. Although I'm not sure if that will work out.
    def run(self):
        while 1:
            size = self.screen.get_cols_rows()
            self.render()
            keys = self.screen.get_input()
            widget, pos = self.widget.get_focus()

            for key in keys:
                self.widget.set_statusmsg('Key: %s (%s)' % (key, pos))
                if key == 'q':
                    transaction.commit()
                    return
                elif key == 'p':
                    return self.create_project()

                self.widget.keypress(size, key)

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
            (project, self.screen), name='editproject').run()

    def contents(self):
        result = []
        for bug in self.context.values():
            widget = urwid.Text(u'%s %s' % (bug.uid, bug.title))
            result.append(urwid.AttrMap(widget, None, 'focus'))
        return urwid.SimpleListWalker(result)


class DashboardWidget(urwid.WidgetWrap):

    body = None
    header = None
    footer = None

    def __init__(self, body, focus='body'):
        self.focus = focus
        self.set_body_content(body)
        self.update_widgets()

    def update_widgets(self):
        self.footer = urwid.Text('', align='left')

        self.header = urwid.AttrMap(urwid.Text(u'Topbar'), 'helpbar')
        self.body_widget = urwid.ListBox(self.body)

        self._w = urwid.Frame(urwid.AttrMap(self.body_widget, 'background'),
                              header=urwid.AttrMap(self.header, 'helpbar'),
                              footer=urwid.AttrMap(self.footer, 'statusbar'))
        self._w.set_focus(self.focus)

    def set_body_content(self, content):
        self.body = content

    def set_statusmsg(self, msg):
        self.footer.set_text(msg)

    def get_focus(self):
        return self.body_widget.get_focus()
