def save(self, *args, **kwargs):
    self.slug = slugify(self.name)[:50]
    return super(Tag, self).save(*args, **kwargs)