def is_in(self, w, mapping):
    r
    p = bisect(mapping, (w,))
    if p > 0:
        if mapping[p - 1][0] == w[:len(mapping[p - 1][0])] and mapping[p - 1][1
            ][:len(w)] == w:
            return True
    if p < len(mapping):
        return mapping[p][0] == w[:len(mapping[p][0])] and mapping[p][1][:
            len(w)] == w
    return False