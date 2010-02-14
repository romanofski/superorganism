import zope.interface
import metatracker.interfaces
import datetime


class ExternalBug(object):

    zope.interface.implements(metatracker.interfaces.IExternalBug)

    id = ''
    url = ''
    status = ''
    component = ''
    assignee = ''
    depends = ''
    blocks = ''

    def __init__(self, id, title, description):
        self.id = self.url = id
        self.title = title
        self.description = description
        self.reported = self.modified = datetime.datetime.today()

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.id)

class Bug(ExternalBug):

    zope.interface.implements(metatracker.interfaces.IBug)
