import doctest
import os
import superorganism.config
import superorganism.database
import superorganism.interfaces
import tempfile
import z3c.testsetup
import zope.component
import zope.interface


OPTIONS = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS

def setUp(test):
    configfile = os.environ.get('configfile')
    cfg_utility = superorganism.config.Configuration(configfile)
    zope.component.provideUtility(cfg_utility,
                                  superorganism.interfaces.IConfiguration)
    storage = superorganism.database.TestDatabase()
    zope.component.provideUtility(storage,
                                  superorganism.interfaces.IDatabase)


class Screen(object):
    """A testing screen which draws the UI as a printout."""

    zope.interface.implements(superorganism.gui.interfaces.IScreen)

    input = []

    def __init__(self):
        self._started = True
        self.has_color = False

    def get_cols_rows(self):
        return (120, 20)

    def draw_screen(self, size, canvas):
        for item in canvas.content():
            # not sure if that's correct
            widgetid, attr, printout = item[0]
            print '%s %s' % (widgetid and '(%s)' %widgetid or '',
                             printout.strip() or '+')

    def get_input(self):
        return self.input

    def register_palette_entry(self, name, fg, bg, mono=None, fghigh=None,
                               bghigh=None):
        print "color palette registered for %s" % name


test_suite = z3c.testsetup.register_all_tests(
    'superorganism', optionflags=OPTIONS)
