def libvlc_video_set_adjust_float(p_mi, option, value):
    f = _Cfunctions.get('libvlc_video_set_adjust_float', None) or _Cfunction(
        'libvlc_video_set_adjust_float', ((1,), (1,), (1,)), None, None,
        MediaPlayer, ctypes.c_uint, ctypes.c_float)
    return f(p_mi, option, value)