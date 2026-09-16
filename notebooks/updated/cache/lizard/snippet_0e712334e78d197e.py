def __deserialize_model(self, data, klass):
    if not klass.swagger_types:
        return data
    kwargs = {}
    for attr, attr_type in iteritems(klass.swagger_types):
        if data is not None and klass.attribute_map[attr
            ] in data and isinstance(data, (list, dict)):
            value = data[klass.attribute_map[attr]]
            kwargs[attr] = self.__deserialize(value, attr_type)
    instance = klass(**kwargs)
    return instance