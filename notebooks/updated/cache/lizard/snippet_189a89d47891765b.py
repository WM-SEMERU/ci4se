def verify_path(path, is_collection):
    num_elements = len(path)
    if num_elements == 0:
        raise ValueError('Document or collection path cannot be empty')
    if is_collection:
        if num_elements % 2 == 0:
            raise ValueError(
                'A collection must have an odd number of path elements')
    elif num_elements % 2 == 1:
        raise ValueError('A document must have an even number of path elements'
            )
    for element in path:
        if not isinstance(element, six.string_types):
            msg = BAD_PATH_TEMPLATE.format(element, type(element))
            raise ValueError(msg)