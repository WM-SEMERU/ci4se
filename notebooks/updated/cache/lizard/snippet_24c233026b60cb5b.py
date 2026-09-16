def firstAnnot(self):
    CheckParent(self)
    val = _fitz.Page_firstAnnot(self)
    if val:
        val.thisown = True
        val.parent = weakref.proxy(self)
        self._annot_refs[id(val)] = val
    return val