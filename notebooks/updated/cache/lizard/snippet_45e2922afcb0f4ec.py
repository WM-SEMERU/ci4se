def objs(self, path=None, model=None, values=None, raise_absent=False):
    return self.search(path=path, unique=False, raise_absent=raise_absent,
        values=values, vfunc=lambda x: self.path_index[x[0]].instance(model
        =model, reraise=False) if x[0] in self.path_index else None)