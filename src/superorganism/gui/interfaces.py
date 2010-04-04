import zope.interface
import zope.schema


class ICharKeyPressEvent(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    key = zope.interface.Attribute(
        "The name of the key pressed.")


class IFunctionKeyPressEvent(ICharKeyPressEvent):
    """Marker interface, that a function key (tab, enter, etc) was
       pressed.
    """


class IKeyDispatcher(zope.interface.Interface):
    """Adapter to dispatch key events."""

    def is_valid_char(key):
        """Determines if a valid char key was pressed."""


class IScreen(zope.interface.Interface):
    """Marker interface for the urwid curses display screen."""


class ITerminalView(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    widget = zope.interface.Attribute("The top most urwid box widget.")

    layout = zope.schema.TextLine(
        title=u'LayoutWidget',
        description=(u'The name of the ILayoutWidget, which is used to'
            ' create the layout of this view.')
    )

    def render():
        """Renders the screen elements."""

    def setup_widgets():
        """Creates and sets up the widget structure."""


class ILayoutWidget(zope.interface.Interface):
    """View widgets define the overall application layout. They're based
       on a Frame, with a header and a footer. The footer is usually a
       statusbar which displays helpful information.
    """

    _w = zope.interface.Attribute("A property to the 'root' widget.")

    def update_widgets(self):
        """Creates the widget internal structure."""

    def get_focus():
        """Returns the current focused widget and it's possition."""


class IProjectForm(zope.interface.Interface):
    """Form for creating a new project."""

    title = zope.schema.TextLine(
        title=u"Projecttitle",
        description=u"The title of the new project."
    )

    description = zope.schema.TextLine(
        title=u"Project Description",
    )

    versions = zope.schema.Set(
        title=u"Versions",
        description=(
            u"A set of possible past and future versions of the project."),
        value_type=zope.schema.TextLine())


class IFormWidget(zope.interface.Interface):
    """Abstract base class for widgets."""

    value = zope.schema.Field(
        title=u'Widget Value',
    )

    label = zope.schema.TextLine(
        title=u'Label',
        description=u'The widgets descriptive label.'
    )

    mode = zope.schema.TextLine(
        title=u'Mode',
        description=u'The mode the widget is in (readonly, input)',
    )

    field = zope.schema.Field(
        title=u'Field',
        description=u'Associated zope.schema Field'
    )

    def update():
        """Updates and creates the (internal) widget structure based on
           urwid widgets.
        """


class IFormFieldWidget(zope.interface.Interface):

    field = zope.schema.Field(
        title=u'Schema Field',
        description=u'Schema field the widget is representing.')


class IContextAware(zope.interface.Interface):

    context = zope.schema.Field(
        title=u'Context',
        description=u'The context in which the widget is displayed.'
    )

    ignoreContext = zope.schema.Bool(
        title=u'Ignore Context',
        description=(u'A flag when set, forces the widget to not look'
                     ' at a context for a value.'),
        default=False,
    )


class IButton(zope.interface.Interface):
    """Marker interface for a button."""

    signals = zope.interface.Attribute(
        "A list of signals associated with the button.")


class ITextInputWidget(IFormWidget):
    """A text input widget providing a title and description, as well as
       an input field.
    """


