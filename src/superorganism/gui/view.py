import zope.interface
import superorganism.gui.interfaces
import superorganism.interfaces


class View(object):

    def __init__(self, context, widget):
        self.context = context
        self.widget = widget

    def render(self):
        raise NotImplementedError(
            "A more specific widget needs to be adapted, "
            "to be able to render any content.")
