def make_dict(self, field_values):
    data_dict = {}
    for key, value, field_type, converter in zip(self.field_names,
        field_values, self.field_types, self.type_converters):
        try:
            data_dict[key] = self.dash_mapper.get(field_type, '-'
                ) if value == '-' else converter(value)
        except ValueError as exc:
            print('Conversion Issue for key:{:s} value:{:s}\n{:s}'.format(
                key, str(value), str(exc)))
            data_dict[key] = value
            if self._strict:
                raise exc
    return data_dict