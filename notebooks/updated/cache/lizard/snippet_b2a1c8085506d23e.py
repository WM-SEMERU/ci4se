def set_parameters(self, parameters_dict):
    DB.set_hash_value(self._key, 'parameters', parameters_dict)
    self.publish('parameters_updated')