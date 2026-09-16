def regex(r):
    if isinstance(r, stringtypes):
        p = re.compile(r)
    else:
        p = r
    msg = 'Expected to match: {}'.format(p.pattern)

    def match_regex(s, grm=None, pos=0):
        m = p.match(s)
        if m is not None:
            start, end = m.span()
            data = m.groupdict() if p.groupindex else m.group()
            return PegreResult(s[m.end():], data, (pos + start, pos + end))
        raise PegreError(msg, pos)
    return match_regex