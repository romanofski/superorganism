import superorganism.interfaces
import zope.component
import zope.interface
import zope.container.contained


class Application(object):

    zope.interface.implements(superorganism.interfaces.IApplication)

    @property
    def dbroot(self):
        db = zope.component.getUtility(superorganism.interfaces.IDatabase)
        return db.root

    def __setitem__(self, key, value):
        zope.container.contained.setitem(
            self, self.dbroot.__setitem__, key, value)

    def __getitem__(self, key):
        return self.dbroot[key]

    def __delitem__(self, key):
        del self.dbroot[key]

    def get(self, name, default=None):
        return self.dbroot.get(name, default)

    def keys(self):
        return self.dbroot.keys()

    def values(self):
        return self.dbroot.values()
