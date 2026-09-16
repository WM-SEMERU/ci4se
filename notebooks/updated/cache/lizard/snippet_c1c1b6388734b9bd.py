def reversed_dotted_parts(s):
    idx = -1
    if s:
        yield s
    while s:
        idx = s.rfind('.', 0, idx)
        if idx == -1:
            break
        yield s[:idx]