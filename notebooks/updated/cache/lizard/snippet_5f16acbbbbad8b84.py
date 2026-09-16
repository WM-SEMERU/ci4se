def _lookup(self, bearer, target=None, permission=None):
    if target is None:
        key = bearer, permission
        lookup = self.bearer
    elif permission is None:
        key = bearer, target
        lookup = self.target
    else:
        key = bearer, target, permission
        lookup = self
    return lookup, key