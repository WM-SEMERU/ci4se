def generate_additional_properties(self):
    self.create_variable_is_dict()
    with self.l('if {variable}_is_dict:'):
        self.create_variable_keys()
        add_prop_definition = self._definition['additionalProperties']
        if add_prop_definition:
            properties_keys = list(self._definition.get('properties', {}).
                keys())
            with self.l('for {variable}_key in {variable}_keys:'):
                with self.l('if {variable}_key not in {}:', properties_keys):
                    self.l('{variable}_value = {variable}.get({variable}_key)')
                    self.generate_func_code_block(add_prop_definition,
                        '{}_value'.format(self._variable), '{}.{{{}_key}}'.
                        format(self._variable_name, self._variable))
        else:
            with self.l('if {variable}_keys:'):
                self.l(
                    'raise JsonSchemaException("{name} must contain only specified properties")'
                    )