def do_get_content(parser, token):
    bits = token.split_contents()
    if not 5 <= len(bits) <= 6:
        raise TemplateSyntaxError('%r expects 4 or 5 arguments' % bits[0])
    if bits[-2] != 'as':
        raise TemplateSyntaxError(
            '%r expects "as" as the second last argument' % bits[0])
    page = parser.compile_filter(bits[1])
    content_type = parser.compile_filter(bits[2])
    varname = bits[-1]
    lang = None
    lang_filter = None
    if len(bits) == 6:
        lang = bits[3]
    else:
        lang_filter = parser.compile_filter('lang')
    return GetContentNode(page, content_type, varname, lang, lang_filter)