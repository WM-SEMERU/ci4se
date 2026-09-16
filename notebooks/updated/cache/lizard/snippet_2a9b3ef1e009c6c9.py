def get_media_stream(self, media_item, format, quality):
    result = self._ajax_api.VideoPlayer_GetStandardConfig(media_id=
        media_item.media_id, video_format=format, video_quality=quality)
    return MediaStream(result)