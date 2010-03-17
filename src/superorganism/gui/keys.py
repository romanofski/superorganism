import zope.interface
import zope.event
import superorganism.gui.interfaces
import urwid


class CharKeyPressed(object):

    zope.interface.implements(superorganism.gui.interfaces.ICharKeyPressEvent)

    def __init__(self, screen, key):
        self.screen = screen
        self.key = key


class FunctionKeyPressed(CharKeyPressed):

    zope.interface.implements(superorganism.gui.interfaces.IFunctionKeyPressEvent)


class Dispatcher(object):

    zope.interface.implements(superorganism.gui.interfaces.IKeyDispatcher)

    def __init__(self, screen):
        self.screen = screen

    def dispatch_key_events(self):
        keys = self.screen.get_input()
        for key in self.screen.get_input():
            if self.is_valid_char(key):
                zope.event.notify(
                    CharKeyPressed(self.screen, key))
            else:
                zope.event.notify(
                    FunctionKeyPressed(self.screen, key))

    def is_valid_char(self, key):
        return urwid.util.is_wide_char(key,0) or (len(key)==1 and ord(key) >= 32)
