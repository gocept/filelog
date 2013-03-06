import os
import stat
import shutil


class Dumper:
    """Saves chronologically ordered dumps of a list of files."""

    def __init__(self, save_prefix, dumpfiles):
        self.prefix = save_prefix
        with open(dumpfiles) as f:
            self.dumpfiles = set(line.strip() for line in f.readlines())

    def prepare_target(self, filename, timestamp):
        """Build dump target filename and create leading directories."""
        target = os.path.join(self.prefix,
                              filename.lstrip('/') + '.' + timestamp)
        try:
            os.makedirs(os.path.dirname(target))
        except OSError:
            pass
        return target

    def dump(self, filename, timestamp):
        if not filename in self.dumpfiles:
            return
        try:
            mode = os.lstat(filename).st_mode
        except OSError:
            return
        if stat.S_ISREG(mode):
            target = self.prepare_target(filename, timestamp)
            shutil.copyfile(filename, target)
        elif stat.S_ISLNK(mode):
            target = self.prepare_target(filename, timestamp)
            os.symlink(os.readlink(filename), target)


class NullDumper(Dumper):
    """Specialized Dumper that does nothing."""

    def __init__(self, *args, **kw):
        pass

    def dump(self, filename):
        pass
