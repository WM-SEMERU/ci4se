def get_docstring_and_rest(filename):
    node, content = parse_source_file(filename)
    if node is None:
        return SYNTAX_ERROR_DOCSTRING, content, 1
    if not isinstance(node, ast.Module):
        raise TypeError('This function only supports modules. You provided {0}'
            .format(node.__class__.__name__))
    if not (node.body and isinstance(node.body[0], ast.Expr) and isinstance
        (node.body[0].value, ast.Str)):
        raise ValueError(
            'Could not find docstring in file "{0}". A docstring is required by sphinx-gallery unless the file is ignored by "ignore_pattern"'
            .format(filename))
    if LooseVersion(sys.version) >= LooseVersion('3.7'):
        docstring = ast.get_docstring(node)
        assert docstring is not None
        if len(node.body[0].value.s) and node.body[0].value.s[0] == '\n':
            docstring = '\n' + docstring
        ts = tokenize.tokenize(BytesIO(content.encode()).readline)
        for tk in ts:
            if tk.exact_type == 3:
                lineno, _ = tk.end
                break
        else:
            lineno = 0
    else:
        docstring_node = node.body[0]
        docstring = docstring_node.value.s
        if hasattr(docstring, 'decode') and not isinstance(docstring, unicode):
            docstring = docstring.decode('utf-8')
        lineno = docstring_node.lineno
    rest = '\n'.join(content.split('\n')[lineno:])
    lineno += 1
    return docstring, rest, lineno