def get_command_line_arguments():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', help=
        "'Displays this help message and exit.'")
    parser.add_argument('-t', '--title', type=unicode, dest='title', help=
        "'Package title.'")
    parser.add_argument('-i', '--input', type=unicode, dest='input', help=
        "'Input file to convert.'")
    parser.add_argument('-o', '--output', type=unicode, dest='output', help
        ="'Output file.'")
    parser.add_argument('-c', '--content_directory', type=unicode, dest=
        'content_directory', help="'Content directory.'")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()