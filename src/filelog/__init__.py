#!python3

from .loop import Loop
from .dump import Dumper, NullDumper
from .event import EventFormatter
import argparse


def cmdline_args():
    argp = argparse.ArgumentParser(description="""\
Monitor directory for all file changes.""")
    argp.add_argument('basedir', metavar='BASEDIR',
                      help='directory to monitor recursively')
    argp.add_argument('-p', '--prefix', default='/tmp/dump',
                      help='dir to dump changed files (default: %(default)s)')
    argp.add_argument('-d', '--dump', metavar='FILE',
                      help='list of filename that should be saved on '
                      'modification')
    return argp.parse_args()


def main():
    args = cmdline_args()
    if args.dump:
        dumper = Dumper(args.prefix, args.dump)
    else:
        dumper = NullDumper()
    loop = Loop(args.basedir, EventFormatter(dumper))
    loop.run_forever()
