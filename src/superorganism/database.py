import ZODB.FileStorage
import ZODB.DemoStorage
import ZODB.DB
import ZODB.config
import superorganism.interfaces
import zope.interface


class Database(object):

    zope.interface.implements(superorganism.interfaces.IDatabase)

    def __init__(self, zconfig):
        self._conn = ZODB.config.databaseFromString(zconfig).open()
        self.root = self._conn.root()


class TestDatabase(Database):

    def __init__(self):
        storage = ZODB.DemoStorage.DemoStorage()
        self._conn = ZODB.DB(storage).open()
        self.root = self._conn.root()
