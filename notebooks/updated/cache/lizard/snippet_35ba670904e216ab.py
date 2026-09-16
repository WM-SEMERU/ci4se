def filter(self, pattern):
    if isinstance(pattern, REGEX_TYPE):
        func = tools.filter_regex
    elif pattern.startswith('/'):
        pattern = re.compile(pattern.strip('/'))
        func = tools.filter_regex
    else:
        func = tools.filter_wildcard
    return SeeResult(func(self, pattern))