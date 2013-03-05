import datetime
import json
import pyinotify


class EventHandler(pyinotify.ProcessEvent):

    def process_default(self, event):
        pathname = event.__dict__.pop('pathname')
        maskname = event.__dict__.pop('maskname')
        event.__dict__.pop('wd')
        event.__dict__.pop('mask')
        event.__dict__.pop('path')
        print('{} {} {} {}'.format(
            datetime.datetime.now().isoformat(),
            pathname, maskname, json.dumps(event.__dict__)))


def main():
    handler = EventHandler()
    mask = (pyinotify.IN_ATTRIB | pyinotify.IN_CLOSE_WRITE |
            pyinotify.IN_CREATE | pyinotify.IN_DELETE |
            pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO)
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, handler)
    wdd = wm.add_watch('/tmp/test', mask, rec=True, auto_add=True)
    notifier.loop()
