def save(self, *args, **kwargs):
    super(ModelDiffMixin, self).save(*args, **kwargs)
    self.__initial = self._dict