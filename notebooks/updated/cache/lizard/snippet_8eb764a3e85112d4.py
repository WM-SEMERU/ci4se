def process_inlines(parser, token):
    args = token.split_contents()
    if not len(args) in (2, 4, 6):
        raise template.TemplateSyntaxError(
            '%r tag requires either 1, 3 or 5 arguments.' % args[0])
    var_name = args[1]
    ALLOWED_ARGS = ['as', 'in']
    kwargs = {'template_directory': None}
    if len(args) > 2:
        tuples = zip(*[args[2:][i::2] for i in range(2)])
        for k, v in tuples:
            if not k in ALLOWED_ARGS:
                raise template.TemplateSyntaxError(
                    '%r tag options arguments must be one of %s.' % (args[0
                    ], ', '.join(ALLOWED_ARGS)))
            if k == 'in':
                kwargs['template_directory'] = v
            if k == 'as':
                kwargs['asvar'] = v
    return InlinesNode(var_name, **kwargs)