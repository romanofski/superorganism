import superorganism.gui.interfaces
import urwid
import zope.interface
import zope.schema.interfaces


class DialogButton(urwid.Button):

    zope.interface.implements(superorganism.gui.interfaces.IButton)

    def __init__(self, label, on_press=None, user_data=None):
        self._label = urwid.SelectableIcon("", 0)
        self._w = urwid.AttrMap(urwid.Columns([
            ('fixed', 1, urwid.Text("<")),
            self._label,
            ('fixed', 1, urwid.Text(">"))],
            dividechars=1), 'button', 'focus')

        # The old way of listening for a change was to pass the callback
        # in to the constructor.  Just convert it to the new way:
        if on_press:
            connect_signal(self, 'click', on_press, user_data)

        self.set_label(label)


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
