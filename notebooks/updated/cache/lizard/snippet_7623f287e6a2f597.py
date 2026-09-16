def add_module_definition(self, module_definition):
    if module_definition.identity not in self._module_definitions.keys():
        self._module_definitions[module_definition.identity
            ] = module_definition
    else:
        raise ValueError('{} has already been defined'.format(
            module_definition.identity))