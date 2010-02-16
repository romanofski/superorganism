import zope.interface
import colony.interfaces


class Project(object):

    zope.interface.implements(colony.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, title, description):
        super(Project, self).__init__()
        self.title = title
        self.description = description
