def default(self, path_spec_object):
    if not isinstance(path_spec_object, path_spec.PathSpec):
        raise TypeError
    json_dict = {'__type__': 'PathSpec'}
    for property_name in path_spec_factory.Factory.PROPERTY_NAMES:
        property_value = getattr(path_spec_object, property_name, None)
        if property_value is not None:
            if property_name == 'row_condition':
                json_dict[property_name] = list(property_value)
            else:
                json_dict[property_name] = property_value
    if path_spec_object.HasParent():
        json_dict['parent'] = self.default(path_spec_object.parent)
    json_dict['type_indicator'] = path_spec_object.type_indicator
    location = getattr(path_spec_object, 'location', None)
    if location:
        json_dict['location'] = location
    return json_dict