def bounding_box_oriented(self):
    from . import primitives, bounds
    to_origin, extents = bounds.oriented_bounds(self)
    obb = primitives.Box(transform=np.linalg.inv(to_origin), extents=
        extents, mutable=False)
    return obb