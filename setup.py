from setuptools import setup, find_packages

version = '0.1'

setup(name='metatracker',
      version=version,
      description=('Metatracker is a bug tracking system which allows to'
                   ' follow/synchronize other bug tracking systems'),
      long_description='',
      keywords='Python',
      author='Roman Joost',
      author_email='roman@bromeco.de',
      url='',
      license='',
      # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Environment :: Web Environment',
                  ],

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['ZConfig',
                        'ZODB3',
                        'setuptools',
                       ],
    entry_points = """
    """
)
