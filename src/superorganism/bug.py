import zope.interface
import zope.component.factory
import superorganism.interfaces
import datetime
import persistent


class Bug(persistent.Persistent):

    zope.interface.implements(superorganism.interfaces.IBug)

    uid = ''
    url = ''
    status = ''
    component = ''
    assignee = ''
    depends = ''
    blocks = ''

    def __init__(self, uid, title, description):
        self.uid = uid
        self.title = title
        self.description = description
        self.reported = self.modified = datetime.datetime.today()

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.uid)


bugFactory = zope.component.factory.Factory(
    Bug,
    title=u'Create a new Bug',
    description=u'Instantiates a new Bug')
