import zope.interface
import colony.interfaces
import persistent


class Project(persistent.Persistent):

    zope.interface.implements(colony.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def add_bug(self, bug):
        app = self.__parent__
        app[bug.id] = bug
