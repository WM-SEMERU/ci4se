def _sanity_check_scale(self, scale_x, scale_y):
    win_wd, win_ht = self.get_window_size()
    if win_wd <= 0 or win_ht <= 0:
        raise ImageViewError('window size undefined')
    if win_wd * scale_x < 1 or win_ht * scale_y < 1:
        raise ValueError(
            'resulting scale (%f, %f) would result in image size of <1 in width or height'
             % (scale_x, scale_y))
    sx = float(win_wd) / scale_x
    sy = float(win_ht) / scale_y
    if sx < 1.0 or sy < 1.0:
        raise ValueError(
            'resulting scale (%f, %f) would result in pixel size approaching window size'
             % (scale_x, scale_y))