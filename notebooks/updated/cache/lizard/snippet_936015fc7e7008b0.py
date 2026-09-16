def get_file_type(filename):
    txt_extensions = ['.txt', '.dat', '.csv']
    hdf_extensions = ['.hdf', '.h5', '.bkup', '.checkpoint']
    for ext in hdf_extensions:
        if filename.endswith(ext):
            with _h5py.File(filename, 'r') as fp:
                filetype = fp.attrs['filetype']
            return filetypes[filetype]
    for ext in txt_extensions:
        if filename.endswith(ext):
            return InferenceTXTFile
    raise TypeError('Extension is not supported.')