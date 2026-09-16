def save(self, *args, **kwargs):
    self.clean()
    if not self.slug:
        self.slug = slugify(self.name)
    super(SpecialCoverage, self).save(*args, **kwargs)
    if self.query and self.query != {}:
        self._save_percolator()