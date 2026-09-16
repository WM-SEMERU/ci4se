def rescale(img, size, mode=None):
    assert size[0] or size[1], 'Must provide a width or a height'
    size = list(size)
    crop = size[0] and size[1]
    if not size[0]:
        size[0] = int(img.size[0] * size[1] / float(img.size[1]))
    if not size[1]:
        size[1] = int(img.size[1] * size[0] / float(img.size[0]))
    if crop:
        b = img.size[0] > img.size[1]
        crop_size = img.size[b], int(img.size[b] * size[0] / float(size[1]))
        if mode == CROP_TL:
            img = img.crop((0, 0, crop_size[0], crop_size[1]))
        elif mode == CROP_BR:
            img = img.crop((img.size[0] - crop_size[0], img.size[1] -
                crop_size[1], img.size[0], img.size[1]))
    return img.resize(size, Image.ANTIALIAS)