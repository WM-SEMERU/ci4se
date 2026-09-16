def __validate_logical(self, operator, definitions, field, value):
    valid_counter = 0
    _errors = errors.ErrorList()
    for i, definition in enumerate(definitions):
        schema = {field: definition.copy()}
        for rule in ('allow_unknown', 'type'):
            if rule not in schema[field] and rule in self.schema[field]:
                schema[field][rule] = self.schema[field][rule]
        if 'allow_unknown' not in schema[field]:
            schema[field]['allow_unknown'] = self.allow_unknown
        validator = self._get_child_validator(schema_crumb=(field, operator,
            i), schema=schema, allow_unknown=True)
        if validator(self.document, update=self.update, normalize=False):
            valid_counter += 1
        else:
            self._drop_nodes_from_errorpaths(validator._errors, [], [3])
            _errors.extend(validator._errors)
    return valid_counter, _errors