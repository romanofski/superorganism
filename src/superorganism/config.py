import zope.interface
import ConfigParser
import superorganism.interfaces


class Configuration(object):

    zope.interface.implements(superorganism.interfaces.IConfiguration)

    def __init__(self, configfile):
        self.reconfigure(configfile)

    def reconfigure(self, configfile):
        conf = ConfigParser.SafeConfigParser()
        conf.read(configfile)
        for name, val in conf.items('app'):
            attr = getattr(self, '_configure_%s' % name)
            if attr is None:
                configure
            attr()

    def _configure
            fg, bg = val.split(',')
            self.tui.register_palette_entry(name, fg.strip(), bg.strip(), None)
        # register projects
        _projects = guiconf.get('app', 'projects')
        for proj in _projects.split('\s'):
            project = superorganism.project.Project(
                guiconf.get(proj, 'title'),
                guiconf.get(proj, 'description'))
            zope.component.provideUtility(project,
                                          superorganism.interfaces.IProject)
