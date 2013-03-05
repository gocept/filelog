filelog
=======

Logs file modifications and optionally dumps changed file contents.

Example:

* list file names which contents should be dumped in a file, for example::

	/etc/ld.so.cache
	/etc/profile.env

* invoke filelog::

	bin/filelog -p /tmp/dump -d myfiles /etc

Modifications are logged to stdout. Content changes of files which are listed in
`myfiles` are dumped beneath /tmp/dump.
