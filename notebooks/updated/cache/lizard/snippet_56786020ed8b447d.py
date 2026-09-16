def qurl(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError('"{0}" takes at least one argument (url)'
            .format(bits[0]))
    if bits.count('|') > 1:
        raise TemplateSyntaxError('"{0}" may take only one separator'.
            format(bits[0]))
    if bits.count('|'):
        url = _get_url_node(parser, bits[:bits.index('|')])
        bits = bits[bits.index('|') + 1:]
    else:
        url = parser.compile_filter(bits[1])
        bits = bits[2:]
    asvar = None
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]
    qs = []
    if len(bits):
        kwarg_re = re.compile('(\\w+)(\\-=|\\+=|=|\\-\\-)(.*)')
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError('Malformed arguments to url tag')
            name, op, value = match.groups()
            qs.append((name, op, parser.compile_filter(value)))
    return QURLNode(url, qs, asvar)