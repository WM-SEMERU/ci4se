def getargs():
    parser = argparse.ArgumentParser(description=
        '    Select paths from a directory tree.')
    parser.add_argument('-a', '--hidden', action='store_false', help=
        'Show all hidden paths too.')
    parser.add_argument('-r', '--relative', action='store_true', help=
        'Output relative paths.')
    parser.add_argument('path', type=chkpath, nargs='?', default='.', help=
        'A valid path.')
    return parser.parse_args()