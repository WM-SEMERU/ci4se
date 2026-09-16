def write_fc3_to_hdf5(fc3, filename='fc3.hdf5', p2s_map=None, compression=None
    ):
    with h5py.File(filename, 'w') as w:
        w.create_dataset('fc3', data=fc3, compression=compression)
        if p2s_map is not None:
            w.create_dataset('p2s_map', data=p2s_map)