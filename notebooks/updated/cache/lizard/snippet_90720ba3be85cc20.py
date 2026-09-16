def write_image_dataset(group, key, data, h5dtype=None):
    if h5dtype is None:
        h5dtype = data.dtype
    if key in group:
        del group[key]
    if group.file.driver == 'core':
        kwargs = {}
    else:
        kwargs = {'fletcher32': True, 'chunks': data.shape}
        kwargs.update(COMPRESSION)
    dset = group.create_dataset(key, data=data.astype(h5dtype), **kwargs)
    dset.attrs.create('CLASS', b'IMAGE')
    dset.attrs.create('IMAGE_VERSION', b'1.2')
    dset.attrs.create('IMAGE_SUBCLASS', b'IMAGE_GRAYSCALE')
    return dset