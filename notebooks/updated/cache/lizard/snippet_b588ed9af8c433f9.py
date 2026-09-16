def get(self, field_path):
    if not self._exists:
        return None
    nested_data = field_path_module.get_nested_value(field_path, self._data)
    return copy.deepcopy(nested_data)