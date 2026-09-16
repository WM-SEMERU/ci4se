def _get_fields(self, attr):
    ret = set()
    if 'OR' in self.pieces:
        return ret
    for i in range(0, len(self.pieces), 2):
        const = self.pieces[i]
        field = getattr(const, attr)
        if field is not None:
            ret.add(field)
    return ret