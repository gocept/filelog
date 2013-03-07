import datetime
import json
import pyinotify
import sys


class EventFormatter(pyinotify.ProcessEvent):
    """Generates log files from inotify events."""

    def __init__(self, dumper, out=sys.stdout):
        super(EventFormatter, self).__init__()
        self.dumper = dumper
        self.out = out

    def process_default(self, event):
        timestamp = datetime.datetime.now().isoformat()
        # fill optional fields with '' to aid output formatting
        for field in ['src_pathname', 'cookie']:
            setattr(event, field, getattr(event, field, ''))
        print('{} {e.pathname} {e.maskname} dir={e.dir} '
              'src={e.src_pathname} cookie={e.cookie}'.format(
              timestamp, e=event), file=self.out)
        self.dumper.dump(event.pathname, timestamp)
