import zope.interface


class IDatabase(zope.interface.Interface):
    """Database utility to store data."""


class IProject(zope.interface.Interface):
    """A project or product holds general information about bugs,
       milestones, etc.
    """

    components = zope.interface.Attribute(
        "The list of components this project has.")

    versions = zope.interface.Attribute(
        "Information about the various versions.")

    title = zope.interface.Attribute(
        "Projectsummary")

    description = zope.interface.Attribute(
        "Short information about the project.")


class IExternalBug(zope.interface.Interface):
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

    description = zope.interface.Attribute(
        "General bug information. How the bug can be reproduced, etc.")

    title = zope.interface.Attribute(
        "A short summary of the bug/problem.")


class IBug(IExternalBug):
    """A problem or error in a software application."""

    id = zope.interface.Attribute("The internal id for the bug.")
