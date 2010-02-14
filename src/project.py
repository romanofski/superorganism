import zope.interface
import metatracker.interfaces


class Project(object):

    zope.interface.implements(metatracker.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, title, description):
        self.title = title
        self.description = description
