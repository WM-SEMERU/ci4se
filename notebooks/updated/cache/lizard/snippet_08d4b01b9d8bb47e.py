def asRGB(self):
    width, height, pixels, info = self.asDirect()
    if info['alpha']:
        raise Error('will not convert image with alpha channel to RGB')
    if not info['greyscale']:
        return width, height, pixels, info
    info['greyscale'] = False
    info['planes'] = 3
    if info['bitdepth'] > 8:

        def newarray():
            return array('H', [0])
    else:

        def newarray():
            return bytearray([0])

    def iterrgb():
        for row in pixels:
            a = newarray() * 3 * width
            for i in range(3):
                a[i::3] = row
            yield a
    return width, height, iterrgb(), info