def get_thumbnail_image(self, page=1):
    url = self.get_thumbnail_image_url(page=page)
    return self._get_url(url)