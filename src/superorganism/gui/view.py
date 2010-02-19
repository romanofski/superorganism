import zope.interface
import zope.component
import superorganism.gui.interfaces


class View(object):

    zope.interface.implements(superorganism.gui.interfaces.IView)
    zope.component.adapts(superorganism.gui.interfaces.IApplication,
                          superorganism.gui.interfaces.IApplication)

    def __init__(self, context, app):
        self.context = context
        self.app = app

    def render(self):
        pass
