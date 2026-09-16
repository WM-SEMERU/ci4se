def _load_h5(filename):
    from neurom.io import hdf5
    return hdf5.read(filename, remove_duplicates=False, data_wrapper=
        DataWrapper)