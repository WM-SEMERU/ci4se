def save_thumbnail(self, thumbnail):
    filename = thumbnail.name
    try:
        self.thumbnail_storage.delete(filename)
    except Exception:
        pass
    self.thumbnail_storage.save(filename, thumbnail)
    thumb_cache = self.get_thumbnail_cache(thumbnail.name, create=True,
        update=True)
    if settings.THUMBNAIL_CACHE_DIMENSIONS:
        dimensions_cache, created = (models.ThumbnailDimensions.objects.
            get_or_create(thumbnail=thumb_cache, defaults={'width':
            thumbnail.width, 'height': thumbnail.height}))
        if not created:
            dimensions_cache.width = thumbnail.width
            dimensions_cache.height = thumbnail.height
            dimensions_cache.save()
    signals.thumbnail_created.send(sender=thumbnail)