def original(self):
    images = self.query._original_images(**self.identity_map)
    if images:
        return images[0]