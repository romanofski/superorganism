import superorganism.database
import superorganism.interfaces
import doctest
import unittest
import zope.testing.doctestunit
import zope.component
import tempfile

APP_CFG = """
[app]
colors = colors
keys = keys

[colors]
statusbar = white, dark cyan,
background = black, white,
focus = black, dark cyan, standout

[keys]
views = BugList
        EditProject
        BugView

[BugView]
f1 = help

[BugList]
f1 = help
f2 = list_bugs

[EditProject]
f1 = help
f10 = quit
"""

def db_setup(test):
    configfile = tempfile.mktemp(suffix='.cfg')
    open(configfile, 'w').write(APP_CFG)
    cfg_utility = superorganism.config.Configuration(configfile)
    zope.component.provideUtility(cfg_utility,
                                  superorganism.interfaces.IConfiguration)
    storage = superorganism.database.TestDatabase()
    zope.component.provideUtility(storage,
                                  superorganism.interfaces.IDatabase)


def test_suite():
    """ returns the test suite """
    return unittest.TestSuite([
        zope.testing.doctestunit.DocFileSuite(
           'bug.txt', package='superorganism',
           optionflags=(
               doctest.COMPARISON_FLAGS |
               doctest.REPORT_ONLY_FIRST_FAILURE)),
        zope.testing.doctestunit.DocFileSuite(
           'project.txt', package='superorganism',
           optionflags=(
               doctest.COMPARISON_FLAGS |
               doctest.REPORT_ONLY_FIRST_FAILURE)),
        zope.testing.doctestunit.DocFileSuite(
           'config.txt', package='superorganism',
           optionflags=(
               doctest.COMPARISON_FLAGS |
               doctest.REPORT_ONLY_FIRST_FAILURE)),
        zope.testing.doctestunit.DocFileSuite(
           'database.txt', package='superorganism',
           optionflags=(doctest.COMPARISON_FLAGS |
                        doctest.REPORT_ONLY_FIRST_FAILURE),
           setUp=db_setup),
    ])

