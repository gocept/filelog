from setuptools import setup, find_packages
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'pyinotify>=0.9.4',
]


setup(name='filelog',
    version=version,
    description="Log file changes in a directory",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Christian Kauhaus',
    author_email='kc@gocept.com',
    url='',
    license='ZPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['filelog=filelog:main']
    }
)
