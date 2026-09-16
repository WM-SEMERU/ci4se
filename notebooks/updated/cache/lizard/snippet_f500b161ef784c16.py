def getChild(self, name, ns=None, default=None):
    if ns is None:
        prefix, name = splitPrefix(name)
        if prefix is not None:
            ns = self.resolvePrefix(prefix)
    for c in self.children:
        if c.match(name, ns):
            return c
    return default