def resolution_phantom(shape=None):
    name = 'phantom_resolution.mat'
    url = URL_CAM + name
    dct = get_data(name, subset=DATA_SUBSET, url=url)
    im = np.rot90(dct['im'], k=3)
    return convert(im, shape)