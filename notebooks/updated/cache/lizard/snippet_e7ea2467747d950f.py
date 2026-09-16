def set_pixel(self, x, y, *args):
    pixel_error = 'Pixel arguments must be given as (r, g, b) or r, g, b'
    if len(args) == 1:
        pixel = args[0]
        if len(pixel) != 3:
            raise ValueError(pixel_error)
    elif len(args) == 3:
        pixel = args
    else:
        raise ValueError(pixel_error)
    if x > 7 or x < 0:
        raise ValueError('X position must be between 0 and 7')
    if y > 7 or y < 0:
        raise ValueError('Y position must be between 0 and 7')
    for element in pixel:
        if element > 255 or element < 0:
            raise ValueError('Pixel elements must be between 0 and 255')
    with open(self._fb_device, 'wb') as f:
        map = self._pix_map[self._rotation]
        f.seek(map[y][x] * 2)
        f.write(self._pack_bin(pixel))