def list_drama_series(self, sort=META.SORT_ALPHA, limit=META.MAX_SERIES,
    offset=0):
    result = self._android_api.list_series(media_type=ANDROID.
        MEDIA_TYPE_DRAMA, filter=sort, limit=limit, offset=offset)
    return result