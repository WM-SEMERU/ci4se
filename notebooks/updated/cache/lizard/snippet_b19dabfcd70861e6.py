def add_cell(self, keypath, cell):
    keypath = keypath[:]
    inner = self
    cellname = keypath
    assert keypath not in self, 'Already exists: %s ' % str(keypath)
    if isinstance(keypath, list):
        while len(keypath) > 1:
            cellname = keypath.pop(0)
            if cellname not in inner:
                inner.__dict__['p'][cellname] = DictCell()
            inner = inner[cellname]
        cellname = keypath[0]
    inner.__dict__['p'][cellname] = cell
    return inner[cellname]