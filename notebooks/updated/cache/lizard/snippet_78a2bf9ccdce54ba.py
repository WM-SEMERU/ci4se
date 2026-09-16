def set_image_dimensions(self, thumbnail):
    try:
        dimensions = getattr(thumbnail, 'dimensions', None)
    except models.ThumbnailDimensions.DoesNotExist:
        dimensions = None
    if not dimensions:
        return False
    self._dimensions_cache = dimensions.size
    return self._dimensions_cache