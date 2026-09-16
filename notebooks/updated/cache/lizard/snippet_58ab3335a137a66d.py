def from_image(cls, image):
    w, h = image.size
    if w > 512:
        ratio = 512.0 / w
        h = int(h * ratio)
        image = image.resize((512, h), Image.ANTIALIAS)
    if image.mode != '1':
        image = image.convert('1')
    pixels = np.array(list(image.getdata())).reshape(h, w)
    extra_rows = int(math.ceil(h / 24)) * 24 - h
    extra_pixels = np.ones((extra_rows, w), dtype=bool)
    pixels = np.vstack((pixels, extra_pixels))
    h += extra_rows
    nb_stripes = h / 24
    pixels = pixels.reshape(nb_stripes, 24, w).swapaxes(1, 2).reshape(-1, 8)
    nh = int(w / 256)
    nl = w % 256
    data = []
    pixels = np.invert(np.packbits(pixels))
    stripes = np.split(pixels, nb_stripes)
    for stripe in stripes:
        data.extend([ESC, 42, 33, nl, nh])
        data.extend(stripe)
        data.extend([27, 74, 48])
    height = h * 2
    return cls(data, height)