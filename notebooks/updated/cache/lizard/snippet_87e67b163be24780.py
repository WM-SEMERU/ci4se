def _get_parser():
    import argparse
    parser = argparse.ArgumentParser(description=
        'Convert between mesh formats.')
    parser.add_argument('infile', type=str, help='mesh file to be read from')
    parser.add_argument('--input-format', '-i', type=str, choices=
        input_filetypes, help='input file format', default=None)
    parser.add_argument('--output-format', '-o', type=str, choices=
        output_filetypes, help='output file format', default=None)
    parser.add_argument('outfile', type=str, help='mesh file to be written to')
    parser.add_argument('--prune', '-p', action='store_true', help=
        'remove lower order cells, remove orphaned nodes')
    parser.add_argument('--prune-z-0', '-z', action='store_true', help=
        'remove third (z) dimension if all points are 0')
    parser.add_argument('--version', '-v', action='version', version=
        '%(prog)s {}, Python {}'.format(__version__, sys.version), help=
        'display version information')
    return parser