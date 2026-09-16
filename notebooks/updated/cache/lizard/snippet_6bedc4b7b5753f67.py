def lower_camel(string, prefix='', suffix=''):
    return require_valid(append_underscore_if_keyword(''.join(word.lower() if
        index == 0 else upper_case_first_char(word) for index, word in
        enumerate(en.words(' '.join([prefix, string, suffix]))))))