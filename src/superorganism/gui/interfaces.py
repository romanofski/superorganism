import zope.interface
import zope.schema


class IKeyPressEvent(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    key_pressed = zope.interface.Attribute(
        "The name of the key pressed.")


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


