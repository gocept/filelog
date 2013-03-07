import datetime
import json
import os
import posix
import pyinotify
import sys


class EventFormatter(pyinotify.ProcessEvent):
    """Generates log files from inotify events."""

    def __init__(self, dumper, out=sys.stdout):
        super(EventFormatter, self).__init__()
        self.dumper = dumper
        self.out = out

    def stat(self, event):
        """Return stat info of changed file or null stat."""
        try:
            return os.lstat(event.pathname)
        except OSError:
            return posix.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    def process_default(self, event):
        timestamp = datetime.datetime.now().isoformat()
        # fill optional fields with '' to aid output formatting
        for field in ['src_pathname', 'cookie']:
            setattr(event, field, getattr(event, field, ''))
        statinfo = self.stat(event)
        print('{ts} {e.pathname} {e.maskname} ino={st.st_ino} '
              'mode={st.st_mode:o} src={e.src_pathname} '
              'cookie={e.cookie}'.format(
              ts=timestamp, st=statinfo, e=event), file=self.out)
        self.dumper.dump(event.pathname, timestamp, statinfo)
