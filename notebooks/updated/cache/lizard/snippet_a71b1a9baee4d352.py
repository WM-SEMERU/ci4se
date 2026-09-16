def encode_example(self, bbox):
    for coordinate in bbox:
        if not isinstance(coordinate, float):
            raise ValueError('BBox coordinates should be float. Got {}.'.
                format(bbox))
        if not 0.0 <= coordinate <= 1.0:
            raise ValueError(
                'BBox coordinates should be between 0 and 1. Got {}.'.
                format(bbox))
        if bbox.xmax < bbox.xmin or bbox.ymax < bbox.ymin:
            raise ValueError('BBox coordinates should have min <= max. Got {}.'
                .format(bbox))
    return super(BBoxFeature, self).encode_example([bbox.ymin, bbox.xmin,
        bbox.ymax, bbox.xmax])