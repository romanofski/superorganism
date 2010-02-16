import colony.database
import colony.interfaces
import doctest
import unittest
import zope.testing.doctestunit
import zope.component


def db_setup(test):
    storage = colony.database.TestDatabase()
    zope.component.provideUtility(storage,
                                   colony.interfaces.IDatabase)

def test_suite():
    """ returns the test suite """
    return unittest.TestSuite([
        zope.testing.doctestunit.DocFileSuite(
           'bug.txt', package='colony',
           optionflags=doctest.COMPARISON_FLAGS | doctest.REPORT_ONLY_FIRST_FAILURE),
        zope.testing.doctestunit.DocFileSuite(
           'project.txt', package='colony',
           optionflags=doctest.COMPARISON_FLAGS | doctest.REPORT_ONLY_FIRST_FAILURE),
        zope.testing.doctestunit.DocFileSuite(
           'database.txt', package='colony',
           optionflags=doctest.COMPARISON_FLAGS | doctest.REPORT_ONLY_FIRST_FAILURE,
           setUp=db_setup),
    ])
