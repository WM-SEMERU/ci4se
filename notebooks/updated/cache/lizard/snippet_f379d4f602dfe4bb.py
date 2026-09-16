def write_hdf5(self, filename, dataset_name=None, info=None, group_name=None):
    r
    from unyt._on_demand_imports import _h5py as h5py
    import pickle
    if info is None:
        info = {}
    info['units'] = str(self.units)
    info['unit_registry'] = np.void(pickle.dumps(self.units.registry.lut))
    if dataset_name is None:
        dataset_name = 'array_data'
    f = h5py.File(filename)
    if group_name is not None:
        if group_name in f:
            g = f[group_name]
        else:
            g = f.create_group(group_name)
    else:
        g = f
    if dataset_name in g.keys():
        d = g[dataset_name]
        if d.shape == self.shape and d.dtype == self.dtype:
            d[...] = self
            for k in d.attrs.keys():
                del d.attrs[k]
        else:
            del f[dataset_name]
            d = g.create_dataset(dataset_name, data=self)
    else:
        d = g.create_dataset(dataset_name, data=self)
    for k, v in info.items():
        d.attrs[k] = v
    f.close()