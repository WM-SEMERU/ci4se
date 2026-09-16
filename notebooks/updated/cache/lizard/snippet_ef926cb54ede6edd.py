def _get_user_input(prompt, key_name, parent, input_func=raw_input):
    val = input_func(prompt)
    ElementTree.SubElement(parent, 'key').text = key_name
    if isinstance(val, bool):
        string_val = 'true' if val else 'false'
        ElementTree.SubElement(parent, string_val)
    else:
        ElementTree.SubElement(parent, 'string').text = val
    return val