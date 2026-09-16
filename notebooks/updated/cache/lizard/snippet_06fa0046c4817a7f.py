def export_data(self):
    data_tuples = ((key, self._serialize(key, value)) for key, value in six
        .iteritems(self._data))
    data_tuples = filter(lambda t: t[1] is not '', data_tuples)
    data = dict(data_tuples)
    return json.dumps(data, separators=(',', ':'))