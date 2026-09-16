def base_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-c', '--config', dest='config', type=argparse.
        FileType('r'), metavar='FILE', help='configuration file')
    parser.add_argument('-o', '--output', dest='output', type=argparse.
        FileType('w'), metavar='FILE', default=sys.stdout, help='output file')
    parser.add_argument('--basedir', dest='basedir', default=os.getcwd(),
        help='base directory')
    parser.add_argument('--input-encoding', dest='input_encoding', default=
        DEFAULT_ENCODING, help='encoding of input source')
    parser.add_argument('--output-encoding', dest='output_encoding',
        default=DEFAULT_ENCODING, help='encoding of output distination')
    parser.add_argument('--processes', dest='processes', type=int, help=
        'number of processes')
    parser.add_argument('--chunksize', dest='chunksize', type=int, default=
        1, help='number of chunks submitted to the process pool')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', dest='verbose', action='count',
        default=0, help='increase logging verbosity')
    group.add_argument('-q', '--quiet', dest='quiet', default=False, action
        ='store_true', help='set logging to quiet mode')
    return parser