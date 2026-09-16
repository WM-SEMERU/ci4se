def delete(self, save=True):
    for thumb in self.field.thumbs:
        thumb_name, thumb_options = thumb
        thumb_filename = self._calc_thumb_filename(thumb_name)
        self.storage.delete(thumb_filename)
    super(ImageWithThumbsFieldFile, self).delete(save)