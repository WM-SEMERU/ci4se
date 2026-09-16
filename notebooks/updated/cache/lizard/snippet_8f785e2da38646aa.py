def nested_tuple(container):
    if isinstance(container, OrderedDict):
        return tuple(map(nested_tuple, container.items()))
    if isinstance(container, Mapping):
        return tuple(sorted_if_possible(map(nested_tuple, container.items())))
    if not isinstance(container, (str, bytes)):
        if isinstance(container, Sequence):
            return tuple(map(nested_tuple, container))
        if isinstance(container, Container) and isinstance(container, Iterable
            ) and isinstance(container, Sized):
            return tuple(sorted_if_possible(map(nested_tuple, container)))
    return container