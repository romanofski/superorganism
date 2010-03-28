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

    def contents(self):
        return []

    def quit(self):
        transaction.commit()
        return
