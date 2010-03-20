import os.path
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '0.1'
setup(name='superorganism',
      version=version,
      description=('Superorganism is a bug tracking system which allows to'
                   ' follow/synchronize other bug tracking systems'),
      long_description = read('README.txt'),
      keywords='Python',
      author='Roman Joost',
      author_email='roman@bromeco.de',
      url='',
      license='',
      # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                  ],

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ZODB3',
          'repoze.zcml',
          'setuptools',
          'urwid',
          'zope.component',
          'zope.container',
      ],
      entry_points = """
    """
)
