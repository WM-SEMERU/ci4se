def extend(self, *schema_items, **kwargs):
    new_kwargs = {'name': self.name, 'doc': self.doc, 'parameters': self.
        _parameters[:], 'result': self.result.copy() if self.result else {},
        'errors': self.errors.copy() if self.errors else set()}
    if 'parameters' in kwargs:
        new_params = kwargs.pop('parameters')
        new_kwargs['parameters'].extend(new_params)
    new_kwargs['result'].update(kwargs.pop('result', {}))
    new_kwargs['errors'].update(kwargs.pop('errors', set()))
    new_kwargs.update(kwargs)
    if schema_items:
        parameters = self._convert_old_schema(schema_items)
        new_kwargs['parameters'].extend(parameters)
    return Schema(**new_kwargs)