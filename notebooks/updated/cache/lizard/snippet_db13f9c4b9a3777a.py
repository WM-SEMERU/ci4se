def promotePrefixes(self):
    for c in self.children:
        c.promotePrefixes()
    if self.parent is None:
        return
    _pref = []
    for p, u in self.nsprefixes.items():
        if p in self.parent.nsprefixes:
            pu = self.parent.nsprefixes[p]
            if pu == u:
                _pref.append(p)
            continue
        if p != self.parent.prefix:
            self.parent.nsprefixes[p] = u
            _pref.append(p)
    for x in _pref:
        del self.nsprefixes[x]
    return self