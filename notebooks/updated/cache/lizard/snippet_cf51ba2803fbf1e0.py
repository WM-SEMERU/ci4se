def display(self, image):
    assert image.mode == self.mode
    assert image.size == self.size
    image = self.preprocess(image)
    i = 0
    d0 = self._const.DIGIT_0
    step = 2 * self.cascaded
    offsets = self._offsets
    rows = self._rows
    buf = bytearray(8 * step)
    pix = list(image.getdata())
    for digit in range(8):
        for daisychained_device in offsets:
            byte = 0
            idx = daisychained_device + digit
            for y in rows:
                if pix[idx] > 0:
                    byte |= 1 << y
                idx += self._w
            buf[i] = digit + d0
            buf[i + 1] = byte
            i += 2
    buf = list(buf)
    for i in range(0, len(buf), step):
        self.data(buf[i:i + step])