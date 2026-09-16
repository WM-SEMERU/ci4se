def feat(self, k, v):
    if not hasattr(self, 'feats'):
        self.feats = {}
        if not hasattr(self, 'featpaths'):
            self.featpaths = {}
    if not k in self.feats:
        self.feats[k] = v
    elif type(self.feats[k]) == type([]):
        self.feats[k].append(v)
    else:
        obj = self.feats[k]
        self.feats[k] = [obj, v]