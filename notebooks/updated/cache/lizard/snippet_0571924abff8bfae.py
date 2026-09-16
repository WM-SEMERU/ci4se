def get_type_data(name):
    name = name.upper()
    if name in CELESTIAL_TIME_TYPES:
        namespace = 'time'
        domain = 'Celestial Time Systems'
        time_name = CELESTIAL_TIME_TYPES[name]
    elif name in EARTH_TIME_TYPES:
        namespace = 'time'
        domain = 'Earth Time Systems'
        time_name = EARTH_TIME_TYPES[name]
    elif name in SUPER_FUN_TIME_TYPES:
        namespace = 'time'
        domain = 'Alternative Time Systems'
        time_name = SUPER_FUN_TIME_TYPES[name]
    else:
        raise NotFound('Time Type: ' + name)
    return {'authority': 'okapia.net', 'namespace': namespace, 'identifier':
        name, 'domain': domain, 'display_name': time_name + ' Time Type',
        'display_label': time_name, 'description': 'The time type for ' +
        time_name + ' time.'}