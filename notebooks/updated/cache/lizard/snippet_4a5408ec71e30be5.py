def enb64_app(parser, cmd, args):
    parser.add_argument('value', help=
        'the value to base64 encode, read from stdin if omitted', nargs='?')
    args = parser.parse_args(args)
    return enb64(pwnypack.main.binary_value_or_stdin(args.value))