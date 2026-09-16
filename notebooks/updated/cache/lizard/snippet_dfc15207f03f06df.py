def libvlc_media_player_new_from_media(p_md):
    f = _Cfunctions.get('libvlc_media_player_new_from_media', None
        ) or _Cfunction('libvlc_media_player_new_from_media', ((1,),),
        class_result(MediaPlayer), ctypes.c_void_p, Media)
    return f(p_md)