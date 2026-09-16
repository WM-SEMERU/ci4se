def get_type_data(name):
    name = name.upper()
    try:
        return {'authority': 'birdland.mit.edu', 'namespace': 'time format',
            'identifier': name, 'domain': 'Time Format Types',
            'display_name': JEFFS_TIME_FORMAT_TYPES[name] +
            ' Time Format Type', 'display_label': JEFFS_TIME_FORMAT_TYPES[
            name], 'description': 'The time format type for ' +
            JEFFS_TIME_FORMAT_TYPES[name]}
    except KeyError:
        raise NotFound('Time Format Type: ' + name)