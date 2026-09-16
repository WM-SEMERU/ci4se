def filter_falsey(data, recurse_depth=None, ignore_types=()):
    filter_element = functools.partial(filter_falsey, recurse_depth=
        recurse_depth - 1, ignore_types=ignore_types
        ) if recurse_depth else lambda x: x
    if isinstance(data, dict):
        processed_elements = [(key, filter_element(value)) for key, value in
            six.iteritems(data)]
        return type(data)([(key, value) for key, value in
            processed_elements if _is_not_considered_falsey(value,
            ignore_types=ignore_types)])
    elif hasattr(data, '__iter__') and not isinstance(data, six.string_types):
        processed_elements = (filter_element(value) for value in data)
        return type(data)([value for value in processed_elements if
            _is_not_considered_falsey(value, ignore_types=ignore_types)])
    return data