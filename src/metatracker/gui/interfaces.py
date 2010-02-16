import zope.interface


class IApplication(zope.interface.Interface):
    """The main application module providing the user interface."""

    def run():
        """The main loop handling key events."""

    def configure(self, config):
        """Configure the application from a user configuration file."""

    def redisplay():
        """Redisplays the applications UI."""

    def set_status(text):
        """Set's a message in the statusbar."""
