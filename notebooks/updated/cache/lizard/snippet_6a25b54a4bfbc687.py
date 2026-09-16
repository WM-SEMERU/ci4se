def _parse_input_parameters(self):
    Global.LOGGER.debug('define and parsing command line arguments')
    parser = argparse.ArgumentParser(description=
        'A workflow engine for Pythonistas', formatter_class=argparse.
        RawTextHelpFormatter)
    parser.add_argument('FILENAME', nargs='+', help=
        'name of the recipe file(s)')
    parser.add_argument('-i', '--INTERVAL', type=int, default=500, metavar=
        'MS', help='perform a cycle each [MS] milliseconds. (default = 500)')
    parser.add_argument('-m', '--MESSAGEINTERVAL', type=int, metavar='X',
        help=
        'dequeue a message each [X] tenth of milliseconds. (default = auto)')
    parser.add_argument('-s', '--STATS', type=int, default=0, metavar='SEC',
        help='show stats each [SEC] seconds. (default = NO STATS)')
    parser.add_argument('-t', '--TRACE', action='store_true', help=
        'enable super verbose output, only useful for tracing')
    parser.add_argument('-v', '--VERBOSE', action='store_true', help=
        'enable verbose output')
    parser.add_argument('-V', '--VERSION', action='version', version=
        __version__)
    args = parser.parse_args()
    return args