def libvlc_media_get_stats(p_md, p_stats):
    f = _Cfunctions.get('libvlc_media_get_stats', None) or _Cfunction(
        'libvlc_media_get_stats', ((1,), (1,)), None, ctypes.c_int, Media,
        ctypes.POINTER(MediaStats))
    return f(p_md, p_stats)