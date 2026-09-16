def render(self, compress=False):
    if not compress and self.original_literal:
        return self.original_literal
    candidates = []
    r, g, b, a = self.value
    r, g, b = int(round(r)), int(round(g)), int(round(b))
    key = r, g, b, a
    if key in COLOR_LOOKUP:
        candidates.append(COLOR_LOOKUP[key])
    if a == 1:
        if all(ch % 17 == 0 for ch in (r, g, b)):
            candidates.append('#%1x%1x%1x' % (r // 17, g // 17, b // 17))
        else:
            candidates.append('#%02x%02x%02x' % (r, g, b))
    else:
        if compress:
            sp = ''
        else:
            sp = ' '
        candidates.append('rgba(%d,%s%d,%s%d,%s%.6g)' % (r, sp, g, sp, b,
            sp, a))
    if compress:
        return min(candidates, key=len)
    else:
        return candidates[0]