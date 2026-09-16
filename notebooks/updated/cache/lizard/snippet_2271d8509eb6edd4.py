def set_image(self, image):
    imwidth, imheight = image.size
    if imwidth != 8 or imheight != 16:
        raise ValueError('Image must be an 8x16 pixels in size.')
    pix = image.convert('1').load()
    for x in xrange(8):
        for y in xrange(16):
            color = pix[x, y]
            if color == 0:
                self.set_pixel(x, y, 0)
            else:
                self.set_pixel(x, y, 1)