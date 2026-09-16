def array_scanlines(self, pixels):
    vpr = self.width * self.planes
    stop = 0
    for y in range(self.height):
        start = stop
        stop = start + vpr
        yield pixels[start:stop]