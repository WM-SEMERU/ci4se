def media_kind(kind):
    if kind in [1]:
        return const.MEDIA_TYPE_UNKNOWN
    if kind in [3, 7, 11, 12, 13, 18, 32]:
        return const.MEDIA_TYPE_VIDEO
    if kind in [2, 4, 10, 14, 17, 21, 36]:
        return const.MEDIA_TYPE_MUSIC
    if kind in [8, 64]:
        return const.MEDIA_TYPE_TV
    raise exceptions.UnknownMediaKind('Unknown media kind: ' + str(kind))