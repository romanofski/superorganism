import zope.interface


class IApplication(zope.interface.Interface):
    """The main application module providing the user interface."""

    def run():
        """The main loop handling key events."""

    def configure(self, config):
        """Configure the application from a user configuration file."""

    def redisplay(name):
        """Redisplays the applications UI."""

    def set_status(text):
        """Set's a message in the statusbar."""


class IKeyPressEvent(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    key_pressed = zope.interface.Attribute(
        "The name of the key pressed.")


class IView(zope.interface.Interface):
    """An adapter providing different views for the application
       depending on the user input.
    """

    def render(self):
        """Renders the screen elements."""


class IWidget(zope.interface.Interface):
    """A widget encapsulating an urwid widget."""

    __parent__ = zope.interface.Attribute("The parent widget.")
