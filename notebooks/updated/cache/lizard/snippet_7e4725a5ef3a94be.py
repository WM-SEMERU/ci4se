def CopyToDict(self):
    path_spec_dict = {}
    for attribute_name, attribute_value in iter(self.__dict__.items()):
        if attribute_value is None:
            continue
        if attribute_name == 'parent':
            attribute_value = attribute_value.CopyToDict()
        path_spec_dict[attribute_name] = attribute_value
    return path_spec_dict