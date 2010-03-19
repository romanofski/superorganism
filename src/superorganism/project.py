import zope.interface
import superorganism.interfaces
import zope.component.factory
import BTrees.OOBTree


class Project(BTrees.OOBTree.OOBTree):

    zope.interface.implements(superorganism.interfaces.IProject)

    components = []
    versions = []

    def __init__(self, uid, title, description):
        super(Project, self).__init__()
        self.uid = uid
        self.title = title
        self.description = description


projectFactory = zope.component.factory.Factory(
    Project,
    title=u'Create a new Project',
    description=u'Instantiates a new Project with uid, title, description')
