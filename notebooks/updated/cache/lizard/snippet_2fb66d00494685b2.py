def _cast_dict(self, data_dict):
    for key, value in data_dict.iteritems():
        data_dict[key] = self._cast_value(value)
    if 'resp_body_data' in data_dict:
        del data_dict['resp_body_data']
    return data_dict