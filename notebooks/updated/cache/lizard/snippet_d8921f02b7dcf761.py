def compare(cls, left, right):
    leftType = TypeOrder.from_value(left).value
    rightType = TypeOrder.from_value(right).value
    if leftType != rightType:
        if leftType < rightType:
            return -1
        return 1
    value_type = left.WhichOneof('value_type')
    if value_type == 'null_value':
        return 0
    elif value_type == 'boolean_value':
        return cls._compare_to(left.boolean_value, right.boolean_value)
    elif value_type == 'integer_value':
        return cls.compare_numbers(left, right)
    elif value_type == 'double_value':
        return cls.compare_numbers(left, right)
    elif value_type == 'timestamp_value':
        return cls.compare_timestamps(left, right)
    elif value_type == 'string_value':
        return cls._compare_to(left.string_value, right.string_value)
    elif value_type == 'bytes_value':
        return cls.compare_blobs(left, right)
    elif value_type == 'reference_value':
        return cls.compare_resource_paths(left, right)
    elif value_type == 'geo_point_value':
        return cls.compare_geo_points(left, right)
    elif value_type == 'array_value':
        return cls.compare_arrays(left, right)
    elif value_type == 'map_value':
        return cls.compare_objects(left, right)
    else:
        raise ValueError('Unknown ``value_type``', str(value_type))