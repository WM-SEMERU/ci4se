def get_type_data(name):
    name = name.upper()
    try:
        return {'authority': 'okapia.net', 'namespace': 'heading',
            'identifier': name, 'domain': 'Headings', 'display_name': 
            HEADING_TYPES[name] + ' Heading Type', 'display_label':
            HEADING_TYPES[name], 'description': 'The heading type for the ' +
            HEADING_TYPES[name] + ' heading.'}
    except KeyError:
        raise NotFound('Heading Type:' + name)