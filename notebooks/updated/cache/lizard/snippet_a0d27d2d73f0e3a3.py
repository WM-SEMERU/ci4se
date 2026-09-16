def to_api_repr(self):
    s_types = {}
    values = {}
    for name, value in self.struct_values.items():
        type_ = self.struct_types[name]
        if type_ in ('STRUCT', 'ARRAY'):
            repr_ = value.to_api_repr()
            s_types[name] = {'name': name, 'type': repr_['parameterType']}
            values[name] = repr_['parameterValue']
        else:
            s_types[name] = {'name': name, 'type': {'type': type_}}
            converter = _SCALAR_VALUE_TO_JSON_PARAM.get(type_)
            if converter is not None:
                value = converter(value)
            values[name] = {'value': value}
    resource = {'parameterType': {'type': 'STRUCT', 'structTypes': [s_types
        [key] for key in self.struct_types]}, 'parameterValue': {
        'structValues': values}}
    if self.name is not None:
        resource['name'] = self.name
    return resource