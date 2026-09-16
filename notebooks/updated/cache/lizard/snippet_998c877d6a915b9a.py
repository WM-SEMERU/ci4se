def get_config(parser=PARSER):
    parser_class = PARSERS[parser]
    _check_parser(parser_class, parser)
    return parser_class.instance()