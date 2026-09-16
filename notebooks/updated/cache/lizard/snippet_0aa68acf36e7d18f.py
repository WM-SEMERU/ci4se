def hdf5_to_dict(filepath, group='/'):
    if not h5py.is_hdf5(filepath):
        raise RuntimeError(filepath, 'is not a valid HDF5 file.')
    with h5py.File(filepath, 'r') as handler:
        dic = walk_hdf5_to_dict(handler[group])
    return dic