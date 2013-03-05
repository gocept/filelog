import datetime
import json
import pyinotify


class EventFormatter(pyinotify.ProcessEvent):
    """Generates log files from inotify events."""

    def process_default(self, event):
        pathname = event.__dict__.pop('pathname')
        maskname = event.__dict__.pop('maskname')
        event.__dict__.pop('wd')
        event.__dict__.pop('mask')
        event.__dict__.pop('path')
        print('{} {} {} {}'.format(
            datetime.datetime.now().isoformat(),
            pathname, maskname, json.dumps(event.__dict__)))
