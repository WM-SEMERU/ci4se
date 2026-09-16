def image_size(self):
    xlen = None
    ylen = None
    for tag in ('Xmp.pyctools.xlen', 'Exif.Photo.PixelXDimension',
        'Exif.Image.ImageWidth', 'Xmp.tiff.ImageWidth'):
        if tag in self.data:
            xlen = int(self.data[tag])
            break
    for tag in ('Xmp.pyctools.ylen', 'Exif.Photo.PixelYDimension',
        'Exif.Image.ImageLength', 'Xmp.tiff.ImageLength'):
        if tag in self.data:
            ylen = int(self.data[tag])
            break
    if xlen and ylen:
        return xlen, ylen
    raise RuntimeError('Metadata does not have image dimensions')