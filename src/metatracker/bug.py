import zope.interface
import metatracker.interfaces
import datetime


class ExternalBug(object):

    zope.interface.implements(metatracker.interfaces.IExternalBug)

    url = ''
    status = ''
    component = ''
    assignee = ''
    depends = ''
    blocks = ''

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.reported = self.modified = datetime.datetime.today()


class Bug(object):

    zope.interface.implements(metatracker.interfaces.IBug)

    id = ''
