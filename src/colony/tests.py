from unittest import TestSuite
from doctest import COMPARISON_FLAGS, REPORT_ONLY_FIRST_FAILURE
from zope.testing import doctestunit


def test_suite():
    """ returns the test suite """
    return TestSuite([
        doctestunit.DocFileSuite(
           'bug.txt', package='colony',
           optionflags=COMPARISON_FLAGS | REPORT_ONLY_FIRST_FAILURE),
        doctestunit.DocFileSuite(
           'project.txt', package='colony',
           optionflags=COMPARISON_FLAGS | REPORT_ONLY_FIRST_FAILURE)
    ])
