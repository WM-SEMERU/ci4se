def _parameter_objects(parameter_objects_from_pillars,
    parameter_object_overrides):
    from_pillars = copy.deepcopy(__salt__['pillar.get'](
        parameter_objects_from_pillars))
    from_pillars.update(parameter_object_overrides)
    parameter_objects = _standardize(_dict_to_list_ids(from_pillars))
    for parameter_object in parameter_objects:
        parameter_object['attributes'] = _properties_from_dict(parameter_object
            ['attributes'])
    return parameter_objects