def null(self, field, **validations):
    values = []
    for found in self._find_by_field(field):
        reality = found['reality']
        schema = {'type': 'null'}
        skip = self._input_boolean(validations.pop('skip', False))
        if not skip:
            self._assert_schema(schema, reality)
        values.append(reality)
    return values