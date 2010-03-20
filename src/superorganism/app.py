import ConfigParser
import os.path
import superorganism.interfaces
import zope.component
import zope.interface


class Application(object):

    zope.interface.implements(superorganism.interfaces.IApplication)

    _colors = []

    def __init__(self, config):
        super(Application, self).__init__()
        self.config = config
        if config:
            self.configure()

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

    def configure(self):
        # XXX that doesn't really belong in here
        confdir = self.config['configdir']
        guiconf = ConfigParser.SafeConfigParser()
        guiconf.read(os.path.join(confdir, 'gui.cfg'))
        for name, val in guiconf.items('colors'):
            fg, bg, mono = val.split(',')
            self._colors.append(
                (name, fg.strip(), bg.strip(), mono.strip()))
        # register projects
        _projects = guiconf.get('app', 'projects')
        for proj in _projects.split('\s'):
            project = superorganism.project.Project(
                guiconf.get(proj, 'id'),
                guiconf.get(proj, 'title'),
                guiconf.get(proj, 'description'))
            zope.component.provideUtility(project,
                                          superorganism.interfaces.IProject)
    @property
    def colors(self):
        return [ colordef for colordef in self._colors ]
