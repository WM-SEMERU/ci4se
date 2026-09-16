def ljust(self, width, fillchar=None):
    if fillchar is not None:
        return fmtstr(self.s.ljust(width, fillchar), **self.shared_atts)
    to_add = ' ' * (width - len(self.s))
    shared = self.shared_atts
    if 'bg' in shared:
        return self + fmtstr(to_add, bg=shared[str('bg')]) if to_add else self
    else:
        uniform = self.new_with_atts_removed('bg')
        return uniform + fmtstr(to_add, **self.shared_atts
            ) if to_add else uniform