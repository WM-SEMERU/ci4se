def libvlc_media_player_has_vout(p_mi):
    f = _Cfunctions.get('libvlc_media_player_has_vout', None) or _Cfunction(
        'libvlc_media_player_has_vout', ((1,),), None, ctypes.c_uint,
        MediaPlayer)
    return f(p_mi)