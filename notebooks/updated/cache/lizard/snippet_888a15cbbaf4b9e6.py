def config_value_keys(self, sortkey=False):
    ret = set()
    cls = type(self)
    while True:
        root = cls.getConfigRoot()
        if root:
            ret = ret.union(set(root.config_value_keys()))
        parent = None
        for c in cls.__bases__:
            if issubclass(c, Configurable):
                parent = c
        if parent is None:
            break
        cls = parent
    if sortkey:
        return sorted(list(ret))
    else:
        return list(ret)