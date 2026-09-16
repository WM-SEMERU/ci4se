def to_column_format(self, high_density_vertical=True):
    im = self._im.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
    line_height = 24 if high_density_vertical else 8
    width_pixels, height_pixels = im.size
    top = 0
    left = 0
    while left < width_pixels:
        box = left, top, left + line_height, top + height_pixels
        im_slice = im.transform((line_height, height_pixels), Image.EXTENT, box
            )
        im_bytes = im_slice.tobytes()
        yield im_bytes
        left += line_height