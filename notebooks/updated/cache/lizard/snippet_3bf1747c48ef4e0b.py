def _replace_fields(self, json_dict):
    for key in self._json_dict.keys():
        if not key.startswith('_'):
            delattr(self, key)
    self._json_dict = json_dict
    self._set_fields(json_dict)