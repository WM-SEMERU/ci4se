def _pixel_data(image):
    if 'PIL.' in str(type(image)):
        pixels = image.tobytes()
        width, height = image.size
    elif 'numpy.ndarray' in str(type(image)):
        if 'uint8' != str(image.dtype):
            image = image.astype('uint8')
        try:
            pixels = image.tobytes()
        except AttributeError:
            pixels = image.tostring()
        height, width = image.shape[:2]
    else:
        pixels, width, height = image
        if 0 != len(pixels) % (width * height):
            raise PyLibDMTXError(
                'Inconsistent dimensions: image data of {0} bytes is not divisible by (width x height = {1})'
                .format(len(pixels), width * height))
    bpp = 8 * len(pixels) // (width * height)
    if bpp not in _PACK_ORDER:
        raise PyLibDMTXError(
            'Unsupported bits-per-pixel: [{0}] Should be one of {1}'.format
            (bpp, sorted(_PACK_ORDER.keys())))
    return pixels, width, height, bpp