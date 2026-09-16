def match_regex(input_str, pattern, language, context, case_insensitive=True):
    if type(context) is str:
        contexts = ['sentence', 'paragraph']
        assert context in contexts or type(context
            ) is int, 'Available contexts: {}'.format(contexts)
    else:
        context = int(context)
    for match in _regex_span(pattern, input_str, case_insensitive=
        case_insensitive):
        if context == 'sentence':
            yield _sentence_context(match, language)
        elif context == 'paragraph':
            yield _paragraph_context(match)
        else:
            yield _window_match(match, context)