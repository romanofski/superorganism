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
