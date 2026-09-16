def get_regex(regex):
    if isinstance(regex, basestring):
        return re.compile(regex)
    elif not isinstance(regex, re._pattern_type):
        raise TypeError('Invalid regex type: %r' % (regex,))
    return regex