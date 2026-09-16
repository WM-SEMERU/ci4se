def _read_dict(self, data_dict, layer=None, source=None):
    for k, v in data_dict.items():
        self._set_with_metadata(k, v, layer, source)