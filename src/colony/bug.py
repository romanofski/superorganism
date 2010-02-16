import zope.interface
import colony.interfaces
import datetime
import persistent


class Bug(persistent.Persistent):

    zope.interface.implements(colony.interfaces.IBug)

    id = ''
    url = ''
    status = ''
    component = ''
    assignee = ''
    depends = ''
    blocks = ''

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.reported = self.modified = datetime.datetime.today()

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.id)
