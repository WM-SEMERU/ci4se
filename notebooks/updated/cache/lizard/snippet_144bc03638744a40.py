def lcsr(s1, s2):
    if s1 == s2:
        return 1.0
    return llcs(s1, s2) / max(1, len(s1), len(s2))