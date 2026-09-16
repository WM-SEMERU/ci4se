def pygmentify(value, **kwargs):
    soup = BeautifulSoup(value, 'html.parser')
    for pre in soup.find_all('pre'):
        code = ''.join([to_string(item) for item in pre.contents])
        code = code.replace('&lt;', '<')
        code = code.replace('&gt;', '>')
        code = code.replace('&#39;', "'")
        code = code.replace('&quot;', '"')
        code = code.replace('&amp;', '&')
        class_list = pre.get('class', [])
        lexers = []
        options = {'stripall': True}
        for c in class_list:
            try:
                lexers.append(get_lexer_by_name(c, **options))
            except ClassNotFound:
                pass
        try:
            lexer = lexers[0]
        except IndexError:
            lexer = None
        if lexer is None:
            try:
                lexer = guess_lexer(pre.text, **options)
                class_list += [alias for alias in lexer.aliases]
            except ClassNotFound:
                pass
        if lexer is not None:
            formatter = HtmlFormatter(**kwargs)
            highlighted = highlight(code, lexer, formatter)
            class_string = ' '.join([c for c in class_list])
            highlighted = highlighted.replace('<div class="%s"><pre>' %
                kwargs['cssclass'], '<div class="%s"><pre class="%s">' % (
                kwargs['cssclass'], class_string))
            pre.replace_with(highlighted)
    return soup.decode(formatter=None).strip()