def _process_config_values(self, dict_path, values, unresolved=[]):
    if isinstance(values, dict):
        for k, v in values.items():
            if not k.isupper():
                del values[k]
                continue
            dict_path.append(''.join(['_', k]))
            if v is None:
                path = ''.join(dict_path)[1:]
                resolved_value = self.resolve_missing_value(k, values, path)
                if resolved_value is None:
                    unresolved.append(path)
                else:
                    values[k] = resolved_value
            elif hasattr(v, '__iter__'):
                self._process_config_values(dict_path, v, unresolved)
            dict_path.pop()
    elif isinstance(values, list):
        for _ in values:
            self._process_config_values(dict_path, _, unresolved)
    return unresolved