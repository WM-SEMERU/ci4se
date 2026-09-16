def _element_format(self, occur):
    if occur:
        occ = occur
    else:
        occ = self.occur
    if occ == 1:
        if hasattr(self, 'default'):
            self.attr['nma:default'] = self.default
        else:
            self.attr['nma:implicit'] = 'true'
    middle = self._chorder() if self.rng_children() else '<empty/>%s'
    fmt = self.start_tag() + self.serialize_annots().replace('%', '%%'
        ) + middle + self.end_tag()
    if (occ == 2 or self.parent.name == 'choice' or self.parent.name ==
        'case' and len(self.parent.children) == 1):
        return fmt
    else:
        return '<optional>' + fmt + '</optional>'