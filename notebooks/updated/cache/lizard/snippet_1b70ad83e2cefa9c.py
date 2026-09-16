def xy_to_rgb(self, x, y, bri=1):
    r, g, b = self.color.get_rgb_from_xy_and_brightness(x, y, bri)
    return r, g, b