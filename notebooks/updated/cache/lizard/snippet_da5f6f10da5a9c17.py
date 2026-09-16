def remote_upload(self, picture_url, resize=None, rotation=None, noexif=None):
    if not resize:
        resize = self._resize
    if not rotation:
        rotation = self._rotation
    if not noexif:
        noexif = self._noexif
    return remote_upload(self._apikey, picture_url, resize, rotation, noexif)