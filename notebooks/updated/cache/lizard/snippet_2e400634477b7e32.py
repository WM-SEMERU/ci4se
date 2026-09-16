def image_url(self, pixel_size=None):
    if 'profile' not in self._raw:
        return
    profile = self._raw['profile']
    if pixel_size:
        img_key = 'image_%s' % pixel_size
        if img_key in profile:
            return profile[img_key]
    return profile[self._DEFAULT_IMAGE_KEY]