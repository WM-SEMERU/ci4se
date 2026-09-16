def write_hdf5_flag(flag, output, path=None, **kwargs):
    if path is None:
        path = flag.name
    if path is None:
        raise ValueError(
            'Cannot determine target group name for flag in HDF5 structure, please set `name` for each flag, or specify the ``path`` keyword when writing'
            )
    return write_hdf5_dict({path: flag}, output, **kwargs)