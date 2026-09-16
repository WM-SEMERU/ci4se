def get_configspec_str(self, index):
    p = index.internalPointer()
    if p is None:
        return
    spec = p.configspec
    if spec is None:
        return None
    k = self.get_key(p, index.row())
    try:
        return spec[k]
    except KeyError:
        return None