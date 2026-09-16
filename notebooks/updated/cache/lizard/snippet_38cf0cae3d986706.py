def addInkAnnot(self, list):
    CheckParent(self)
    val = _fitz.Page_addInkAnnot(self, list)
    if not val:
        return
    val.thisown = True
    val.parent = weakref.proxy(self)
    self._annot_refs[id(val)] = val
    return val