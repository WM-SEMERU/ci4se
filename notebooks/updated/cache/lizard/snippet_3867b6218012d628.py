def _parse_dict(element, definition):
    sub_dict = {}
    for name, subdef in viewitems(definition):
        name, required = _parse_name(name)
        sub_dict[name] = xml_to_json(element, subdef, required)
    return sub_dict