def main(args=None):
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--binary', dest='mode', action='store_const',
        const='wb', default='w', help='write in binary mode')
    parser.add_argument('output', metavar='FILE', type=unicode, help=
        'Output file')
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format=
        '[%(levelname)s elapsed=%(relativeCreated)dms] %(message)s')
    args = parser.parse_args(args or sys.argv[1:])
    with open(args.output, args.mode) as fd:
        for line in sys.stdin:
            fd.write(line)