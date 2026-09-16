def execute_with_style_LEGACY(template, style, data, callback, body_subtree
    ='body'):
    try:
        body_data = data[body_subtree]
    except KeyError:
        raise EvaluationError('Data dictionary has no subtree %r' %
            body_subtree)
    tokens_body = []
    template.execute(body_data, tokens_body.append)
    data[body_subtree] = tokens_body
    tokens = []
    style.execute(data, tokens.append)
    _FlattenToCallback(tokens, callback)