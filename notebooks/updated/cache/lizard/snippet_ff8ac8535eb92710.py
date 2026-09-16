def _already_resized_on_fb(self, fn, pid, _megapixels):
    logger.debug('%s - resize requested' % fn)
    width_fb, height_fb = self._getphoto_originalsize(pid)
    new_width, new_height = pusher_utils.resize_compute_width_height(fn,
        _megapixels)
    logger.debug('%s - fb %d/%d, current %d/%d' % (fn, width_fb, height_fb,
        new_width, new_height))
    if width_fb == new_width and height_fb == new_height:
        return True
    elif width_fb == new_height and height_fb == new_width:
        return True
    return False