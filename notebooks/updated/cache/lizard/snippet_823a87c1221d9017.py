def scale_and_shift_cmap(self, scale_pct, shift_pct):
    rgbmap = self.get_rgbmap()
    rgbmap.scale_and_shift(scale_pct, shift_pct)