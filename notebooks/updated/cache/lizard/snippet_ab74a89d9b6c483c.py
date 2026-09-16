def libvlc_media_player_set_time(p_mi, i_time):
    f = _Cfunctions.get('libvlc_media_player_set_time', None) or _Cfunction(
        'libvlc_media_player_set_time', ((1,), (1,)), None, None,
        MediaPlayer, ctypes.c_longlong)
    return f(p_mi, i_time)