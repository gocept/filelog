from .loop import Loop
import argparse


def main():
    argp = argparse.ArgumentParser(description="""\
Monitor directory for all file changes.""")
    argp.add_argument('basedir', metavar='BASEDIR',
                      help='directory to monitor recursively')
    args = argp.parse_args()
    loop = Loop(args.basedir)
    loop.run_forever()
