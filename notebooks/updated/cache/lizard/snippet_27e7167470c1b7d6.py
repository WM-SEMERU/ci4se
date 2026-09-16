def lookup_symbol(self, sname, skind=list(SharedData.KINDS.keys()), stype=
    list(SharedData.TYPES.keys())):
    skind = skind if isinstance(skind, list) else [skind]
    stype = stype if isinstance(stype, list) else [stype]
    for i, sym in [[x, self.table[x]] for x in range(len(self.table) - 1,
        SharedData.LAST_WORKING_REGISTER, -1)]:
        if sym.name == sname and sym.kind in skind and sym.type in stype:
            return i
    return None