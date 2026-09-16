def camelcase(text, acronyms=None):
    words, _case, _sep = case_parse.parse_case(text, acronyms)
    if words:
        words[0] = words[0].lower()
    return ''.join(words)