import zope.interface
import ConfigParser
import os.path
import superorganism.interfaces


class Configuration(object):

    zope.interface.implements(superorganism.interfaces.IConfiguration)

    def __init__(self, configfile):
        self.conf = ConfigParser.SafeConfigParser()
        if not os.path.exists(configfile):
            raise IOError("Supplied configfile doesn't exist: %s" %
                          configfile)
        self.conf.read(configfile)

    def configure_colors(self, screen):
        for name, val in self.conf.items('colors'):
            fg, bg, mono = val.split(',')
            mono = mono.strip()
            if not mono:
                mono = None
            screen.register_palette_entry(
                name, fg.strip(), bg.strip(), mono)

    def get_registered_views(self):
        pass

    def get_keys_for(self, viewname):
        pass
