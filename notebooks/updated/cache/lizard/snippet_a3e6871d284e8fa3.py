def default_classification_value_maps(classification):
    value_maps = {}
    for hazard_class in classification['classes']:
        value_maps[hazard_class['key']] = hazard_class.get('string_defaults',
            [])
    return value_maps