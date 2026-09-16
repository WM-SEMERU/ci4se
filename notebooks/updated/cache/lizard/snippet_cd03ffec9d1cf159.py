def dotted_parts(s):
    idx = -1
    while s:
        idx = s.find('.', idx + 1)
        if idx == -1:
            yield s
            break
        yield s[:idx]