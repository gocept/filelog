# python3.2

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


version = '0.1'

install_requires = [
    'pyinotify>=0.9.4',
]


setup(
    name='filelog',
    version=version,
    description="Log file changes in a directory",
    classifiers=[
        'Programming Language :: Python :: 3.2',
        'Environment :: Console',
    ],
    keywords='',
    author='Christian Kauhaus',
    author_email='kc@gocept.com',
    url='',
    license='ZPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['filelog=filelog:main']
    }
)
