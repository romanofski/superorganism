import ConfigParser
import os.path
import superorganism.interfaces
import zope.component
import zope.interface
import BTrees.OOBTree


class Application(BTrees.OOBTree.OOBTree):

    zope.interface.implements(superorganism.interfaces.IApplication)

    _colors = []

    def __init__(self, config):
        super(Application, self).__init__()
        self.config = config
        if config:
            self.configure()

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
