def dict_to_hdf5(dic, endpoint):
    filename = gen_filename(endpoint)
    with h5py.File(filename, 'w') as handler:
        walk_dict_to_hdf5(dic, handler)
    print('dumped to', filename)