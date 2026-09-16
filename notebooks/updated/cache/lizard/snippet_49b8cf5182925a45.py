def get_type_data(name):
    name = name.upper()
    if name in ISO_CURRENCY_TYPES:
        article = 'the '
        type_name = ISO_CURRENCY_TYPES[name]
    elif name in ISO_CURRENCY_ELEMENT_TYPES:
        article = ''
        type_name = ISO_CURRENCY_ELEMENT_TYPES[name]
    else:
        raise NotFound('Currency Type: ' + name)
    return {'authority': 'ISO', 'namespace': '4217', 'identifier': name,
        'domain': 'ISO Currency Types', 'display_name': type_name +
        ' Currency Type', 'display_label': type_name, 'description': 
        'The ISO currency type for ' + article + type_name + '.'}