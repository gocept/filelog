# python3.2

from setuptools import setup, find_packages

version = '0.1'

setup(
    name='filelog',
    version=version,
    description="Log file changes in a directory",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.2',
        'Topic :: System :: Systems Administration',
    ],
    keywords='',
    author='Christian Kauhaus',
    author_email='kc@gocept.com',
    url='https://bitbucket.org/gocept/filelog',
    license='ZPL-2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyinotify>=0.9.4',
    ],
    entry_points={
        'console_scripts': ['filelog=filelog:main']
    }
)
