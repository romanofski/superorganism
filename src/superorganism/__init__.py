import os.path
import zope.configuration.xmlconfig

path = os.path.join(os.path.dirname(__file__), 'configure.zcml')
ctx = zope.configuration.xmlconfig.file(path)
