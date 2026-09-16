def set_element_attributes(elem_to_parse, **attrib_kwargs):
    element = get_element(elem_to_parse)
    if element is None:
        return element
    if len(attrib_kwargs):
        element.attrib.update(attrib_kwargs)
    return element.attrib