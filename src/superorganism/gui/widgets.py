import superorganism.gui.interfaces
import urwid
import zope.interface
import zope.schema.interfaces
import zope.component.factory


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


class FormWidget(urwid.WidgetWrap):

    zope.interface.implements(superorganism.gui.interfaces.IFormWidget)

    name = ''
    __name__ = ''
    label = ''
    widgetfactory = 'superorganism.gui.widgets.default'
    value = ''
    field = None
    context = None
    ignoreContext = False
    required = False

    def __init__(self, screen):
        self.screen = screen

    def update(self):
        value = ''
        if (superorganism.gui.interfaces.IFormFieldWidget.providedBy(self)\
            and not self.field.missing_value):
            self.value = self.field.default
        if (superorganism.gui.interfaces.IContextAware.providedBy(self)\
            and self.ignoreContext == False):
            self.value = self.field.get(self.context)
        self._w = zope.component.getUtility(
            zope.component.interfaces.IFactory, name=self.widgetfactory)(self)

    @property
    def description(self):
        desc = ''
        if superorganism.gui.interfaces.IFormFieldWidget.providedBy(self):
            desc = self.field.description
        return desc

    def extract(self):
        return self._w.extract()


def FormFieldWidget(field, widget):
    widget.field = field
    if not superorganism.gui.interfaces.IFormFieldWidget.providedBy(widget):
        zope.interface.alsoProvides(
            widget, superorganism.gui.interfaces.IFormFieldWidget)
    widget.__name__ = field.__name__
    widget.label = field.title
    widget.required = field.required
    widget.update()
    return widget


class TextInputWidgetLayout(urwid.WidgetWrap):

    zope.interface.implements(superorganism.gui.interfaces.ILayoutWidget)

    def __init__(self, widget, mode='input'):
        self.widget = widget
        self.mode = mode
        self.update_widgets()

    def update_widgets(self):
        text = urwid.Text(self.widget.label)
        self.edit = urwid.Edit(edit_text=self.widget.value or '', edit_pos=0)
        desc = urwid.Text(self.widget.description)
        self._w = urwid.AttrMap(
            urwid.Columns([text,
                           ('weight', 3, urwid.AttrMap(self.edit, self.mode)),
                           desc]), None, 'focus')

    def extract(self):
        return self.edit.get_text()[0]


textinputwidgetlayout = zope.component.factory.Factory(
    TextInputWidgetLayout,
    title=u'New textinput widget layout')


@zope.component.adapter(zope.schema.TextLine,
                        superorganism.gui.interfaces.IScreen)
@zope.interface.implementer(superorganism.gui.interfaces.IFormFieldWidget)
def TextInputFieldWidget(field, screen):
    formwidget = FormWidget(screen)
    formwidget.widgetfactory = 'superorganism.gui.widgets.textinput'
    return FormFieldWidget(field, formwidget)


# XXX
@zope.component.adapter(zope.schema.Set,
                        superorganism.gui.interfaces.IScreen)
@zope.interface.implementer(superorganism.gui.interfaces.IFormFieldWidget)
def TextareaFieldWidget(field, screen):
    formwidget = FormWidget(screen)
    formwidget.widgetfactory = 'superorganism.gui.widgets.textinput'
    return FormFieldWidget(field, formwidget)
