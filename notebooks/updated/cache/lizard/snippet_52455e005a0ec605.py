def max_layout_dimensions(dimensions):
    min_ = max([d.min for d in dimensions if d.min is not None])
    max_ = max([d.max for d in dimensions if d.max is not None])
    preferred = max([d.preferred for d in dimensions])
    return LayoutDimension(min=min_, max=max_, preferred=preferred)