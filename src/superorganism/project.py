import zope.interface
import superorganism.interfaces


class Project(object):

    zope.interface.implements(superorganism.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, uid, title, description):
        super(Project, self).__init__()
        self.uid = uid
        self.title = title
        self.description = description

