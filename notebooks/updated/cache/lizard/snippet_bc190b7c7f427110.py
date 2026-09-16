def xml_to_json(element, definition, required=False):
    if isinstance(definition, str) and len(definition) > 0:
        if definition[0] == '@':
            return element.get(definition[1:])
        else:
            sub_element = element.find(definition)
            if sub_element is None:
                if required:
                    raise NotCompleteXmlException(
                        'Expecting {0} in element {1}'.format(definition,
                        element.tag))
                return None
            return sub_element.text.strip() if sub_element.text else None
    elif isinstance(definition, tuple):
        return _parse_tuple(element, definition, required)
    elif isinstance(definition, dict):
        return _parse_dict(element, definition)
    elif isinstance(definition, list):
        return _parse_list(element, definition)
    elif hasattr(definition, '__call__'):
        return definition(element)
    else:
        return element.text.strip() if element.text else None