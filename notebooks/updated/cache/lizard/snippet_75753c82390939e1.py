def libvlc_media_new_location(p_instance, psz_mrl):
    f = _Cfunctions.get('libvlc_media_new_location', None) or _Cfunction(
        'libvlc_media_new_location', ((1,), (1,)), class_result(Media),
        ctypes.c_void_p, Instance, ctypes.c_char_p)
    return f(p_instance, psz_mrl)