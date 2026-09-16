def loadLinks(self):
    CheckParent(self)
    val = _fitz.Page_loadLinks(self)
    if val:
        val.thisown = True
        val.parent = weakref.proxy(self)
        self._annot_refs[id(val)] = val
        if self.parent.isPDF:
            val.xref = self._getLinkXrefs()[0]
        else:
            val.xref = 0
    return val