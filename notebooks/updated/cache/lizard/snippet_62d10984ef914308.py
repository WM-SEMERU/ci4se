def blurring_kernel(shape=None):
    name = 'motionblur.mat'
    url = URL_CAM + name
    dct = get_data(name, subset=DATA_SUBSET, url=url)
    return convert(255 - dct['im'], shape, normalize='sum')