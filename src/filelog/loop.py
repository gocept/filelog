import pyinotify


class Loop:

    MASK = (pyinotify.IN_ATTRIB | pyinotify.IN_CLOSE_WRITE |
            pyinotify.IN_CREATE | pyinotify.IN_DELETE |
            pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO)

    def __init__(self, base, eventhandler):
        self.base = base
        self.eventhandler = eventhandler

    def run_forever(self):
        manager = pyinotify.WatchManager()
        notifier = pyinotify.Notifier(manager, self.eventhandler)
        manager.add_watch(self.base, self.MASK, rec=True, auto_add=True)
        notifier.loop()
