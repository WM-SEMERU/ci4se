def to_png(self, transparent=True, thumbnail_size=None, resampling=None,
    in_range='dtype', out_range='dtype'):
    return self.to_bytes(transparent=transparent, thumbnail_size=
        thumbnail_size, resampling=resampling, in_range=in_range, out_range
        =out_range)