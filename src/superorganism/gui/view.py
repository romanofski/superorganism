import superorganism.gui.app
import superorganism.gui.interfaces
import zope.interface
import transaction


class BaseView(object):

    zope.interface.implements(superorganism.gui.interfaces.ITerminalView)
    widget = None

    def __init__(self, context, screen):
        self.context = context
        self.screen = screen
        self.setup_widgets()

    def __call__(self):
        self.render()

    def render(self):
        size = self.screen.get_cols_rows()
        canvas = self.widget.render(size, focus=True)
        self.screen.draw_screen(size, canvas)

    def setup_widgets(self):
        self.widget = superorganism.gui.interfaces.ILayoutWidget(self)

    def run(self):
        util = zope.component.getUtility(
            superorganism.interfaces.IConfiguration)
        while 1:
            size = self.screen.get_cols_rows()
            self.render()
            keys = self.screen.get_input()
            widget, pos = self.widget.get_focus()

            for key in keys:
                self.widget.set_statusmsg('Key: %s (%s)' %(key, widget))
                mapping = util.get_keys_for(self.__class__.__name__)
                if mapping.has_key(key):
                    return getattr(self, mapping[key])()
                self.widget.keypress(size, key)

    def contents(self):
        return []

    def quit(self):
        transaction.commit()
        return
