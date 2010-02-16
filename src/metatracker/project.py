import zope.interface
import metatracker.interfaces
import persistent


class Project(persistent.Persistent):

    zope.interface.implements(metatracker.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def add_bug(self, bug):
        app = self.__parent__
        app[bug.id] = bug
