import zope.interface


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


class IDashboard(IView):
    """Dashboard screen."""


class IScreen(zope.interface.Interface):
    """Marker interface for the urwid curses display screen."""
