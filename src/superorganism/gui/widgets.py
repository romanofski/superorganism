import superorganism.gui.interfaces
import urwid
import zope.interface
import zope.schema.interfaces


class BaseFormWidget(urwid.WidgetWrap):

    def __init__(self, field, form):
        self.field = field
        self.form = form
        self._value = field.get(form.context)
        self.update()

    def update(self):
        raise NotImplementedError("Implemented in subclasses.")

    def set(self, value):
        self.field.set(self.form.context, value)

    @property
    def value(self):
        return self.field.get(self.form.context)


class TextInputWidget(BaseFormWidget):

    zope.interface.implements(superorganism.gui.interfaces.ITextInputWidget)

    def __init__(self, field, form):
        self.field = field
        self.form = form
        self._value = field.get(form.context)
        self.update()

    def update(self):
        text = urwid.Text(self.field.title)
        edit = urwid.AttrMap(
            urwid.Edit(edit_text=self._value, edit_pos=0), 'input')
        edit.highlight = (0, len(self._value))
        desc = urwid.Text(self.field.description)
        self._w = urwid.AttrMap(
            urwid.Columns([text, ('weight', 3, edit), desc]), None,
            'focus')

    def set(self, value):
        self.field.set(self.form.context, value)

    @property
    def value(self):
        return self.field.get(self.form.context)


class MultilineInputWidget(urwid.WidgetWrap):

    zope.interface.implements(superorganism.gui.interfaces.ITextInputWidget)

    def update(self):
        text = urwid.Text(self.field.title)
        edit = urwid.AttrMap(
            urwid.Edit(edit_text=self._value, multiline=True, edit_pos=0),'input')
        edit.highlight = (0, len(self._value))
        desc = urwid.Text(self.field.description)
        self._w = urwid.AttrMap(
            urwid.Columns([text, ('weight', 3, edit), desc]), None,
            'focus')
