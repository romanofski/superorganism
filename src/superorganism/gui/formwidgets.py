import superorganism.gui.interfaces
import urwid
import zope.component.factory
import zope.interface


class TextInputWidget(urwid.WidgetWrap):

    zope.interface.implements(superorganism.gui.interfaces.ITextInputWidget)

    def __init__(self, title, description='', value=''):
        self.title = title
        self.description = description
        self._value = value
        self.update()

    def update(self):
        text = urwid.Text(self.title)
        edit = urwid.AttrMap(
            urwid.Edit(edit_text=self._value, edit_pos=0), None, 'input')
        edit.highlight = (0, len(self._value))
        desc = urwid.Text(self.description)
        self._w = urwid.AttrMap(
            urwid.Columns([text, ('weight', 3, edit), desc]), None,
            'focus')

    def set(self, value):
        self._value = value

    @property
    def value(self):
        return self._value



textinputFactory = zope.component.factory.Factory(
    TextInputWidget,
    title=u'Creates a new text input widget',
    description=u'Instantiates a new input widget')
