import ZODB.FileStorage
import ZODB.DemoStorage
import ZODB.DB
import superorganism.interfaces
import zope.interface


class Database(object):

    zope.interface.implements(superorganism.interfaces.IDatabase)

    def __init__(self, config):
        storage = ZODB.FileStorage.FileStorage(config['database'])
        self._conn = ZODB.DB(storage).open()
        self.root = self._conn.root()


class TestDatabase(Database):

    def __init__(self):
        storage = ZODB.DemoStorage.DemoStorage()
        self._conn = ZODB.DB(storage).open()
        self.root = self._conn.root()
