def _GetDataTypeMap(self, name):
    data_type_map = self._data_type_maps.get(name, None)
    if not data_type_map:
        data_type_map = self._fabric.CreateDataTypeMap(name)
        self._data_type_maps[name] = data_type_map
    return data_type_map