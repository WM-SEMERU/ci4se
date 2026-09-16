def asRGB(self):
    width, height, pixels, meta = self.asDirect()
    if meta['alpha']:
        raise Error('will not convert image with alpha channel to RGB')
    if not meta['greyscale']:
        return width, height, pixels, meta
    meta['greyscale'] = False
    typecode = 'BH'[meta['bitdepth'] > 8]

    def iterrgb():
        for row in pixels:
            a = array(typecode, [0]) * 3 * width
            for i in range(3):
                a[i::3] = row
            yield a
    return width, height, iterrgb(), meta