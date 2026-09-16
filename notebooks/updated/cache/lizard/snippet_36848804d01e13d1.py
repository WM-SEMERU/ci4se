def writeNSdict(self, nsdict):
    for k, v in nsdict.items():
        if (k, v) in _standard_ns:
            continue
        rv = _reserved_ns.get(k)
        if rv:
            if rv != v:
                raise KeyError('Reserved namespace ' + str((k, v)) + ' used')
            continue
        if k:
            self.dom.setNamespaceAttribute(k, v)
        else:
            self.dom.setNamespaceAttribute('xmlns', v)