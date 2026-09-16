def cycle_find_app(_parser, cmd, args):
    parser = argparse.ArgumentParser(prog=_parser.prog, description=_parser
        .description)
    parser.add_argument('-w', '--width', type=int, default=4, help=
        'the length of the cycled value')
    parser.add_argument('value', help=
        'the value to determine the position of, read from stdin if missing',
        nargs='?')
    args = parser.parse_args(args)
    index = cycle_find(pwnypack.main.string_value_or_stdin(args.value),
        args.width)
    if index == -1:
        print('Not found.')
        sys.exit(1)
    else:
        print('Found at position: %d' % index)