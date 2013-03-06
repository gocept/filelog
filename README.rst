filelog
=======

Logs file modifications and optionally dumps changed file contents.


Invocation
----------

Log all file modifications beneath `/etc`::

   bin/filelog /etc

As long as `filelog` is running, it will log a track record of all file
modifications to stdout.


Dumping changed files
---------------------

List full path names of all files which should be dumped in a file, called
`dumpfiles` in the following example::

   /etc/ld.so.cache
   /etc/profile

Then, invoke `filelog` with this file and a prefix under which the dumps should
be placed::

   filelog -d dumpfiles -p /tmp/dumpster /etc

Each time a file which is named in `dumpfiles` gets modified, a new copy is
made and saved in `/tmp/dumpster`.
