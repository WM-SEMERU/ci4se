def parse_image_name(self, image):
    self._image = image
    self.uri = self.get_uri(image)
    self.image = self.remove_uri(image)