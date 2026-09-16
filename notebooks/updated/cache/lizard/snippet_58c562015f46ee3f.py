def add_to_set(original_set, element):
    if not element:
        return original_set
    if isinstance(element, Set):
        original_set |= element
    elif isinstance(element, (list, tuple)):
        original_set |= set(element)
    else:
        original_set.add(element)
    return original_set