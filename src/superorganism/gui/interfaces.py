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


class ITerminalView(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    def render():
        """Renders the screen elements."""


class IDashboard(ITerminalView):
    """Dashboard screen."""

    def create_project():
        """Creates a new project."""


class IScreen(zope.interface.Interface):
    """Marker interface for the urwid curses display screen."""


class IForm(ITerminalView):
    """Base class for forms."""

    def update_widgets(self):
        """Create widgets and set them up."""


class INewProjectForm(IForm):
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


class IWidget(zope.interface.Interface):
    """Abstract base class for widgets."""

    value = zope.interface.Attribute("The widget value")

    def update():
        """Updates and creates the (internal) widget structure based on
           urwid widgets.
        """

    def set(value):
        """Set the widget text to value."""


class ITextInputWidget(IWidget):
    """A text input widget providing a title and description, as well as
       an input field.
    """

