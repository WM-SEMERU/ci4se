def ndimage_to_list(image):
    inpixeltype = image.pixeltype
    dimension = image.dimension
    components = 1
    imageShape = image.shape
    nSections = imageShape[dimension - 1]
    subdimension = dimension - 1
    suborigin = iio.get_origin(image)[0:subdimension]
    subspacing = iio.get_spacing(image)[0:subdimension]
    subdirection = np.eye(subdimension)
    for i in range(subdimension):
        subdirection[(i), :] = iio.get_direction(image)[(i), 0:subdimension]
    subdim = image.shape[0:subdimension]
    imagelist = []
    for i in range(nSections):
        img = utils.slice_image(image, axis=subdimension, idx=i)
        iio.set_spacing(img, subspacing)
        iio.set_origin(img, suborigin)
        iio.set_direction(img, subdirection)
        imagelist.append(img)
    return imagelist