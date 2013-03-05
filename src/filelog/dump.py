import os
import time
import shutil


class Dumper:
    """Saves chronologically ordered dumps of a list of files."""

    def __init__(self, save_prefix, dumpfiles):
        self.prefix = save_prefix
        with open(dumpfiles) as f:
            self.dumpfiles = set(line.strip() for line in f.readlines())

    def dump(self, filename):
        if not filename in self.dumpfiles:
            return
        self.save(filename)

    def save(self, filename):
        target = os.path.join(self.prefix,
                              filename.lstrip('/') + '.' + str(time.time()))
        try:
            os.makedirs(os.path.dirname(target))
        except OSError:
            pass
        shutil.copyfile(filename, target)
