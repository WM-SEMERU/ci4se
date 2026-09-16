def get_structure(element, reference=None):
    if reference is None:
        try:
            reference = load_reference(element.name, element.classname,
                element.version)
        except (ChildNotFound, KeyError):
            raise InvalidName(element.classname, element.name)
    if not isinstance(reference, collections.Sequence):
        raise Exception
    return ElementFinder._parse_structure(element, reference)