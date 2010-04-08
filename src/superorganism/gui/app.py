import superorganism.gui.interfaces
import superorganism.gui.view
import superorganism.gui.widgets
import superorganism.interfaces
import superorganism.project
import urwid
import zope.component
import zope.component.interfaces
import zope.interface


class ApplicationLayout(urwid.WidgetWrap):

    zope.interface.implements(superorganism.gui.interfaces.ILayoutWidget)
    zope.component.adapts(superorganism.gui.interfaces.ITerminalView)

    body = None
    header = None
    footer = None

    def __init__(self, view):
        self.focus = 'body'
        self.view = view
        self.update_widgets()

    def update_widgets(self):
        keybar = KeyConfigurationWidget(self.view)
        self.status = urwid.Text('', align='left')
        footer = urwid.Pile([keybar, self.status])

        self.header = urwid.AttrMap(urwid.Text(u'Topbar'), 'helpbar')
        self.body = urwid.ListBox(self.create_body())

        self._w = urwid.Frame(urwid.AttrMap(self.body, 'background'),
                              header=urwid.AttrMap(self.header, 'helpbar'),
                              footer=urwid.AttrMap(footer, 'statusbar'))
        self._w.set_focus(self.focus)

    def create_body(self):
        result = []
        for bug in self.view.context.values():
            widget = urwid.Text(u'%s' % (bug.title))
            result.append(urwid.AttrMap(widget, None, 'focus'))
        return urwid.SimpleListWalker(result)

    def set_statusmsg(self, msg):
        self.status.set_text(msg)

    def get_focus(self):
        return self.body.get_focus()


class KeyConfigurationWidget(urwid.WidgetWrap):

    def __init__(self, view):
        self.view = view
        self.update_widgets()

    def update_widgets(self):
        cfg = zope.component.getUtility(
            superorganism.interfaces.IConfiguration)
        name = self.view.__class__.__name__
        widgets = []
        for key,val in cfg.get_keys_for(name).items():
            widget = urwid.Columns([
                ('fixed', 3, urwid.AttrMap(urwid.Text(key.upper()), 'input')),
                urwid.AttrMap(urwid.Text(val), 'focus'),
            ])
            widgets.append(widget)
        self._w = urwid.Columns(widgets)

    def get_focus(self):
        return self._w.get_focus()
