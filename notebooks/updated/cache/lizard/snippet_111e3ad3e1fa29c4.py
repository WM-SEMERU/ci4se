def __match_l(self, k, _set):
    return {r for r in _set if k[0] in range(*r) or k[1] in range(*r) or k[
        0] < r[0] and k[1] >= r[1]}