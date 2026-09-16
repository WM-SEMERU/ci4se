def get_range(self, i):
    try:
        m = i.match(RE_INT_ITER)
        if m:
            return self.get_int_range(*m.groups())
        m = i.match(RE_CHR_ITER)
        if m:
            return self.get_char_range(*m.groups())
    except Exception:
        pass
    return None