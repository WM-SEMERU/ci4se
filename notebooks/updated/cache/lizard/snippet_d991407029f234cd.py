def astype(self, data_type):
    data_type = types.validate_data_type(data_type)
    if data_type == self._data_type:
        return self
    attr_dict = dict()
    attr_dict['_data_type'] = data_type
    attr_dict['_source_data_type'] = self._source_data_type
    attr_dict['_input'] = self
    new_sequence = AsTypedSequenceExpr(**attr_dict)
    return new_sequence