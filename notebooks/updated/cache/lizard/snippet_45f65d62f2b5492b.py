def _arevalid(self, datatype):
    if datatype not in self.meta:
        return datatype in Dap._optional_meta, []
    if datatype in self._required_meta and not self.meta[datatype]:
        return False, []
    if not isinstance(self.meta[datatype], list):
        return False, []
    duplicates = set([x for x in self.meta[datatype] if self.meta[datatype]
        .count(x) > 1])
    if duplicates:
        return False, list(duplicates)
    if datatype in self._badmeta:
        return False, self._badmeta[datatype]
    else:
        return True, []
    bad = []
    for item in self.meta[datatype]:
        if not Dap._meta_valid[datatype].match(item):
            bad.append(item)
    return len(bad) == 0, bad