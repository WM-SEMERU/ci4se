def DeregisterDefinition(self, data_type_definition):
    name = data_type_definition.name.lower()
    if name not in self._definitions:
        raise KeyError('Definition not set for name: {0:s}.'.format(
            data_type_definition.name))
    del self._definitions[name]