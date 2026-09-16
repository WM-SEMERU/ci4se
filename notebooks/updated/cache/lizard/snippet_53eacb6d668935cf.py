def do_macro(parser, token):
    try:
        bits = token.split_contents()
        tag_name, macro_name, arguments = bits[0], bits[1], bits[2:]
    except IndexError:
        raise template.TemplateSyntaxError(
            "'{0}' tag requires at least one argument (macro name)".format(
            token.contents.split()[0]))
    arg_regex = '^([A-Za-z_][\\w_]*)$'
    kwarg_regex = ('^([A-Za-z_][\\w_]*)=(".*"|{0}.*{0}|[A-Za-z_][\\w_]*)$'.
        format("'"))
    args = []
    kwargs = {}
    for argument in arguments:
        arg_match = regex_match(arg_regex, argument)
        if arg_match:
            args.append(arg_match.groups()[0])
        else:
            kwarg_match = regex_match(kwarg_regex, argument)
            if kwarg_match:
                kwargs[kwarg_match.groups()[0]] = template.Variable(kwarg_match
                    .groups()[1])
            else:
                raise template.TemplateSyntaxError(
                    'Malformed arguments to the {0} tag.'.format(tag_name))
    nodelist = parser.parse(('endmacro',))
    parser.delete_first_token()
    _setup_macros_dict(parser)
    parser._macros[macro_name] = DefineMacroNode(macro_name, nodelist, args,
        kwargs)
    return parser._macros[macro_name]