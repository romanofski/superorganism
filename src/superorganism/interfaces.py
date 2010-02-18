import zope.interface


class IConfiguration(zope.interface.Interface):
    """Low-level application configuration utility."""

    def reconfigure(configfile):
        """Reconfigure the application by reloading the configuration or
           reading another configuration file.
        """


class IDatabase(zope.interface.Interface):
    """Database utility to store data."""


class IContent(zope.interface.Interface):
    """Basic content object for the bug tracker."""

    uid = zope.interface.Attribute(
        "A unique ID identifying this object.")

    title = zope.interface.Attribute(
        "Content title")

    description = zope.interface.Attribute(
        "Short information this content.")


class IApplication(IContent):
    """The application content object."""


class IProject(IContent):
    """A project or product holds general information about bugs,
       milestones, etc.
    """

    components = zope.interface.Attribute(
        "The list of components this project has.")

    versions = zope.interface.Attribute(
        "Information about the various versions.")


class IBug(IContent):
    """A problem or error in a software application, which holds
       information about an external bug.
    """

    url = zope.interface.Attribute("The URL to the bug.")

    status = zope.interface.Attribute(
        "The internal status of the bug (e.g. Unconfirmed, open, etc)")

    component = zope.interface.Attribute(
        "The product component this bug belongs to (e.g. UI, "
        "Internationalisation, General)")

    assignee = zope.interface.Attribute(
        "Which person is responsible for this bug.")

    depends = zope.interface.Attribute(
        "Which other bug this bug depends on to get it fixed.")

    blocks = zope.interface.Attribute(
        "Which other bug this bug blocks.")

    reported = zope.interface.Attribute(
        "On which date was this bug reported.")

    modified = zope.interface.Attribute(
        "Which was the last modification date of this bug.")

