def _add_sub_elements_from_dict(parent, sub_dict):
    for key, value in sub_dict.items():
        if isinstance(value, list):
            for repeated_element in value:
                sub_element = ET.SubElement(parent, key)
                _add_element_attrs(sub_element, repeated_element.get(
                    'attrs', {}))
                children = repeated_element.get('children', None)
                if isinstance(children, dict):
                    _add_sub_elements_from_dict(sub_element, children)
                elif isinstance(children, str):
                    sub_element.text = children
        else:
            sub_element = ET.SubElement(parent, key)
            _add_element_attrs(sub_element, value.get('attrs', {}))
            children = value.get('children', None)
            if isinstance(children, dict):
                _add_sub_elements_from_dict(sub_element, children)
            elif isinstance(children, str):
                sub_element.text = children