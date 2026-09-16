def libvlc_media_player_set_media(p_mi, p_md):
    f = _Cfunctions.get('libvlc_media_player_set_media', None) or _Cfunction(
        'libvlc_media_player_set_media', ((1,), (1,)), None, None,
        MediaPlayer, Media)
    return f(p_mi, p_md)