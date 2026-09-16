def attach_photo(self, photo: String, caption: String=None):
    self.media.attach_photo(photo, caption)
    return self