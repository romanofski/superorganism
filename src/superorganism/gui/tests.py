import doctest
import os.path
import superorganism.gui.interfaces
import unittest
import zope.component
import zope.testing.doctestunit


def test_suite():
    """ returns the test suite """
    return unittest.TestSuite([
        zope.testing.doctestunit.DocFileSuite(
           os.path.join('gui','views.txt'),
           package='superorganism',
           optionflags=(
               doctest.COMPARISON_FLAGS |
               doctest.REPORT_ONLY_FIRST_FAILURE)),
    ])
