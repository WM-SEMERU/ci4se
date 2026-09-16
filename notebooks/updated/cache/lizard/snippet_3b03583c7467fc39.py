def libvlc_video_get_spu(p_mi):
    f = _Cfunctions.get('libvlc_video_get_spu', None) or _Cfunction(
        'libvlc_video_get_spu', ((1,),), None, ctypes.c_int, MediaPlayer)
    return f(p_mi)