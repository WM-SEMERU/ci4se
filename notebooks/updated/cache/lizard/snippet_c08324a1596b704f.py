def dict_from_hdf5(dict_like, h5group):
    for name, value in h5group.attrs.items():
        dict_like[name] = value