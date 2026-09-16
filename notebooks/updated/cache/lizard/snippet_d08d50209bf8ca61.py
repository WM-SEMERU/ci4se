def _add_default_entries(input_dict, defaults_dict):
    for key, value in defaults_dict.iteritems():
        if key == 'patients':
            print('Cannot default `patients`.')
            continue
        if isinstance(value, dict):
            if key not in input_dict or input_dict[key] is None:
                input_dict[key] = value
            else:
                r = _add_default_entries(input_dict.get(key, {}), value)
                input_dict[key] = r
        elif key not in input_dict or input_dict[key] is None:
            input_dict[key] = value
    return input_dict