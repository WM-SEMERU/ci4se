def video_get_cursor(self, num=0):
    r = libvlc_video_get_cursor(self, num)
    if isinstance(r, tuple) and len(r) == 2:
        return r
    raise VLCException('invalid video number (%s)' % (num,))