def libvlc_video_set_subtitle_file(p_mi, psz_subtitle):
    f = _Cfunctions.get('libvlc_video_set_subtitle_file', None) or _Cfunction(
        'libvlc_video_set_subtitle_file', ((1,), (1,)), None, ctypes.c_int,
        MediaPlayer, ctypes.c_char_p)
    return f(p_mi, psz_subtitle)