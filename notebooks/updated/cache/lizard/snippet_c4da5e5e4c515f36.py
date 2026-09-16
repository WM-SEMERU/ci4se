def _one_contains_other(s1, s2):
    return min(len(s1), len(s2)) == len(s1 & s2)