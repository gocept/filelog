import datetime
import json
import pyinotify


class EventFormatter(pyinotify.ProcessEvent):
    """Generates log files from inotify events."""

    def __init__(self, dumper):
        super(EventFormatter, self).__init__()
        self.dumper = dumper

    def process_default(self, event):
        data = dict(event.__dict__)
        pathname = data.pop('pathname')
        maskname = data.pop('maskname').lstrip('IN_')
        data.pop('wd')
        data.pop('mask')
        data.pop('path')
        print('{} {} {} {}'.format(
            datetime.datetime.now().isoformat(),
            pathname, maskname, json.dumps(data)))
        self.dumper.dump(pathname)
