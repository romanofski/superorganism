import doctest
import os.path
import superorganism.gui.interfaces
import unittest
import zope.component
import zope.testing.doctestunit
import superorganism.tests


def test_suite():
    """ returns the test suite """
    return unittest.TestSuite([
        zope.testing.doctestunit.DocFileSuite(
            'views.txt',
            package='superorganism.gui',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
        ),
        zope.testing.doctestunit.DocFileSuite(
            'app.txt',
            package='superorganism.gui',
            optionflags=(
                doctest.NORMALIZE_WHITESPACE |
                doctest.ELLIPSIS |
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
            setUp=superorganism.tests.db_setup),
        zope.testing.doctestunit.DocFileSuite(
            'projects.txt',
            package='superorganism.gui',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
        ),
        zope.testing.doctestunit.DocFileSuite(
            'formwidgets.txt',
            package='superorganism.gui',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
            setUp=superorganism.tests.db_setup,
        ),
        zope.testing.doctestunit.DocFileSuite(
            'keys.txt',
            package='superorganism.gui',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
        ),
    ])


class Screen(object):
    """A testing screen which draws the UI as a printout."""

    zope.interface.implements(superorganism.gui.interfaces.IScreen)

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
        return ['q']

    def register_palette_entry(self, name, fg, bg, mono=None, fghigh=None,
                               bghigh=None):
        print "color palette registered for %s" % name
