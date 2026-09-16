def apply_mtd(self, mtd, *args, cont=False, tag=None, **kwargs):
    new_lhs = getattr(self.lhs, mtd)(*args, **kwargs)
    if new_lhs == self.lhs and cont:
        new_lhs = None
    new_rhs = getattr(self.rhs, mtd)(*args, **kwargs)
    new_tag = tag
    return self._update(new_lhs, new_rhs, new_tag, cont)