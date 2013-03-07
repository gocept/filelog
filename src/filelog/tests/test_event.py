from filelog.dump import NullDumper
from filelog.event import EventFormatter
import io
import datetime
import unittest


TIMESTAMP = datetime.datetime(2013, 3, 7, 8, 32, 18)


class CreateDirEvent:

    maskname = 'IN_CREATE|IN_ISDIR'
    pathname = '/tmp/test'
    name = 'test'
    path = '/tmp'
    dir = True


class RenameEvent:

    maskname = 'IN_MOVED_TO'
    pathname = '/tmp/file2'
    src_pathname = '/tmp/file1'
    name = 'file2'
    path = '/tmp'
    dir = False
    cookie = 859


class EventFormatterTest(unittest.TestCase):

    def test_logline_create(self):
        capture = io.StringIO()
        ef = EventFormatter(NullDumper(), capture)
        ef.process_default(CreateDirEvent())
        self.assertRegex(capture.getvalue(),
                         r'^[0-9T:.-]+ /tmp/test IN_CREATE\|IN_ISDIR '
                         r'dir=True src= cookie=')

    def test_logline_rename(self):
        capture = io.StringIO()
        ef = EventFormatter(NullDumper(), capture)
        ef.process_default(RenameEvent())
        self.assertRegex(capture.getvalue(),
                         r'^[0-9T:.-]+ /tmp/file2 IN_MOVED_TO '
                         r'dir=False src=/tmp/file1 cookie=859')
