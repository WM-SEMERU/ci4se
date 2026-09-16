def apply2parser(cmd_proxy, parser):
    if isinstance(cmd_proxy, CmdProxy):
        parser_proxy = cmd_proxy.meta.parser
        _apply2parser(parser_proxy.arguments, parser_proxy.options, parser)
    return parser