def literals(choices, prefix='', suffix=''):
    return '|'.join(prefix + re.escape(c) + suffix for c in choices.split())