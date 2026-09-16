def make_parser():
    parser = argparse.ArgumentParser(description=
        'generate HTML from crawler JSON')
    parser.add_argument('--data-dir', default='data', help=
        'Directory containing JSON data from crawler [%(default)s]')
    parser.add_argument('--output-dir', default='html', help=
        'Directory to output the resulting HTML files [%(default)s]')
    return parser