import ConfigParser
import os.path
import superorganism.interfaces
import zope.component
import zope.interface


class Application(object):

    zope.interface.implements(superorganism.interfaces.IApplication)

    def __init__(self, config):
        super(Application, self).__init__()

    @property
    def dbroot(self):
        db = zope.component.getUtility(superorganism.interfaces.IDatabase)
        return db.root

    def __setitem__(self, key, value):
        self.dbroot[key] = value

    def __getitem__(self, key):
        return self.dbroot[key]

    def __delitem__(self, key):
        del self.dbroot[key]

    def keys(self):
        return self.dbroot.keys()

    def values(self):
        return self.dbroot.values()
