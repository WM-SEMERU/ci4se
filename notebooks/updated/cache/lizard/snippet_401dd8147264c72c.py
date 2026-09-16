def get_module_config(self, name):
    if self.exists('modules'):
        if name in self._json['modules'] and not isinstance(self._json[
            'modules'][name], str):
            return self._json['modules'][name]
    return None