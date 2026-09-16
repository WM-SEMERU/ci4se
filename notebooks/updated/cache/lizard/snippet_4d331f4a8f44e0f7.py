def get_or_add_media_part(self, media):
    media_part = self._find_by_sha1(media.sha1)
    if media_part is None:
        media_part = MediaPart.new(self._package, media)
    return media_part