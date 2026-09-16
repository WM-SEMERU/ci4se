def bounding_cylinder(self):
    from . import primitives, bounds
    kwargs = bounds.minimum_cylinder(self)
    mincyl = primitives.Cylinder(mutable=False, **kwargs)
    return mincyl