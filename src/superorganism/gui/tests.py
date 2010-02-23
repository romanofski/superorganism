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
            os.path.join('gui','views.txt'),
            package='superorganism',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
            setUp=superorganism.tests.db_setup),
        zope.testing.doctestunit.DocFileSuite(
            os.path.join('gui','app.txt'),
            package='superorganism',
            optionflags=(
                doctest.COMPARISON_FLAGS |
                doctest.REPORT_ONLY_FIRST_FAILURE),
            setUp=superorganism.tests.db_setup),
    ])


class Screen(object):
    """A testing screen which draws the UI as a printout."""

    zope.interface.implements(superorganism.gui.interfaces.IScreen)

    def __init__(self):
        self._started = True
        self.has_color = False

    def get_cols_rows(self):
        return (80, 20)

    def draw_screen(self, size, canvas):
        for item in canvas.content():
            # not sure if that's correct
            widgetid, attr, printout = item[0]
            if not widgetid:
                widgetid = '|'
            print '(%s) %s' % (widgetid, printout.strip())
