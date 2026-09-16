def libvlc_media_get_meta(p_md, e_meta):
    f = _Cfunctions.get('libvlc_media_get_meta', None) or _Cfunction(
        'libvlc_media_get_meta', ((1,), (1,)), string_result, ctypes.
        c_void_p, Media, Meta)
    return f(p_md, e_meta)