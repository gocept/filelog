from .loop import Loop
from .dump import Dumper
import argparse


def main():
    argp = argparse.ArgumentParser(description="""\
Monitor directory for all file changes.""")
    argp.add_argument('basedir', metavar='BASEDIR',
                      help='directory to monitor recursively')
    argp.add_argument('-p', '--prefix', help='dir to dump changed files in')
    argp.add_argument('-d', '--dump', metavar='FILE',
                      help='whitelist of filename that should be saved on '
                      'modification')
    args = argp.parse_args()
    dumper = Dumper(args.prefix, args.dump)
    loop = Loop(args.basedir, dumper)
    loop.run_forever()
