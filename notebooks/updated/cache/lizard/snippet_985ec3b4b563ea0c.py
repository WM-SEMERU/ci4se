def handle_token(cls, parser, token):
    tag_error = (
        'Accepted formats {%% %(tagname)s %(args)s %%} or {%% %(tagname)s %(args)s as [var] %%}'
        )
    bits = token.split_contents()
    args_count = len(bits) - 1
    if args_count >= 2 and bits[-2] == 'as':
        as_var = bits[-1]
        args_count -= 2
    else:
        as_var = None
    if args_count != cls.args_count:
        arg_list = ' '.join(['[arg]' * cls.args_count])
        raise TemplateSyntaxError(tag_error % {'tagname': bits[0], 'args':
            arg_list})
    args = [parser.compile_filter(tkn) for tkn in bits[1:args_count + 1]]
    return cls(args, varname=as_var)