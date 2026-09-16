def cli_script_main(cli_args):
    choices = ALL_UNIT_TYPES
    parser = argparse.ArgumentParser(description=
        'Converts from one type of size to another.')
    parser.add_argument('--from-stdin', default=False, action='store_true',
        help='Reads number from stdin rather than the cli')
    parser.add_argument('-f', '--from', choices=choices, nargs=1, type=str,
        dest='fromunit', default=['Byte'], help=
        'Input type you are converting from. Defaultes to Byte.')
    parser.add_argument('-t', '--to', choices=choices, required=False,
        nargs=1, type=str, help=
        'Input type you are converting to. Attempts to detect best result if omitted.'
        , dest='tounit')
    parser.add_argument('size', nargs='*', type=float, help=
        'The number to convert.')
    args = parser.parse_args(cli_args)
    if args.from_stdin:
        args.size = [float(sys.stdin.readline()[:-1])]
    results = []
    for size in args.size:
        instance = getattr(__import__('bitmath', fromlist=['True']), args.
            fromunit[0])(size)
        if args.tounit:
            result = getattr(instance, args.tounit[0])
        else:
            result = instance.best_prefix()
        results.append(result)
    return results