def addSquigglyAnnot(self, rect):
    CheckParent(self)
    val = _fitz.Page_addSquigglyAnnot(self, rect)
    if not val:
        return
    val.thisown = True
    val.parent = weakref.proxy(self)
    self._annot_refs[id(val)] = val
    return val