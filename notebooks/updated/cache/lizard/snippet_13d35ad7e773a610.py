def dimension_name(dimension):
    if isinstance(dimension, Dimension):
        return dimension.name
    elif isinstance(dimension, basestring):
        return dimension
    elif isinstance(dimension, tuple):
        return dimension[0]
    elif isinstance(dimension, dict):
        return dimension['name']
    elif dimension is None:
        return None
    else:
        raise ValueError(
            '%s type could not be interpreted as Dimension. Dimensions must be declared as a string, tuple, dictionary or Dimension type.'
             % type(dimension).__name__)