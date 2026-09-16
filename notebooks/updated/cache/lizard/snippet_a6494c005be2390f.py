def verify(path):
    valid = False
    try:
        h5 = h5py.File(path, mode='r')
    except (OSError, IsADirectoryError):
        pass
    else:
        if 'file_format' in h5.attrs and h5.attrs['file_format'].lower(
            ) == 'hyperspy' and 'Experiments' in h5:
            valid = True
    return valid