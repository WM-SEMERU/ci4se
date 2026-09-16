def setup(argv):
    parser = argparse.ArgumentParser(description=
        'Compute Jekyl- and prose-aware wordcounts', epilog=
        'Accepted filetypes: plaintext, markdown, markdown (Jekyll)')
    parser.add_argument('-S', '--split-hyphens', action='store_true', dest=
        'split_hyphens', help=
        'split hyphenated words rather than counting them as one word ("non-trivial" counts as two words rather than one)'
        )
    parser.add_argument('-u', '--update', action='store_true', help=
        'update the jekyll file in place with the counts. Does nothing if the file is not a Jekyll markdown file. Implies format=yaml, invalid with input from STDIN and non-Jekyll files.'
        )
    parser.add_argument('-f', '--format', nargs='?', choices=['yaml',
        'json', 'default'], default='default', help='output format.')
    parser.add_argument('-i', '--indent', type=int, nargs='?', default=4,
        help='indentation depth (default: 4).')
    parser.add_argument('file', type=argparse.FileType('rb'), help=
        'file to parse (or - for STDIN)')
    return parser.parse_args(argv)