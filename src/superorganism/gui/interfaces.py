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

    def render():
        """Renders the screen elements."""

    def contents():
        """Returns the contents (as widget(s)) used to display in the
           setup ILayoutWidget.
        """


class ILayoutWidget(zope.interface.Interface):
    """View widgets define the overall application layout. They're based
       on a Frame, with a header and a footer. The footer is usually a
       statusbar which displays helpful information.
    """

    def update_widgets(self):
        """Creates the widget internal structure."""

    def get_focus():
        """Returns the current focused widget and it's possition."""


class INewProjectForm(ITerminalView):
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

    value = zope.interface.Attribute("The widget value")

    def update():
        """Updates and creates the (internal) widget structure based on
           urwid widgets.
        """

    def set(value):
        """Set the widget text to value."""


class IButton(zope.interface.Interface):
    """Marker interface for a button."""

    signals = zope.interface.Attribute(
        "A list of signals associated with the button.")


class ITextInputWidget(IFormWidget):
    """A text input widget providing a title and description, as well as
       an input field.
    """


