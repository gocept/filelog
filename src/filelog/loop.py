from .event import EventFormatter
import pyinotify


class Loop:

    MASK = (pyinotify.IN_ATTRIB | pyinotify.IN_CLOSE_WRITE |
            pyinotify.IN_CREATE | pyinotify.IN_DELETE |
            pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO)

    def __init__(self, base):
        self.base = base

    def run_forever(self):
        manager = pyinotify.WatchManager()
        notifier = pyinotify.Notifier(manager, EventFormatter())
        manager.add_watch(self.base, self.MASK, rec=True, auto_add=True)
        notifier.loop()
