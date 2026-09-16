def applyaty(self, content, xty):
    name = 'type'
    ns = Namespace.xsins
    parent = content.node
    for child in parent.getChildren():
        ref = child.get(name, ns)
        if ref is None:
            parent.addPrefix(ns[0], ns[1])
            attr = ':'.join((ns[0], name))
            child.set(attr, xty)
    return self