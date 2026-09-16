def _EvaluateElementsDataSize(self, context):
    elements_data_size = None
    if self._data_type_definition.elements_data_size:
        elements_data_size = self._data_type_definition.elements_data_size
    elif self._data_type_definition.elements_data_size_expression:
        expression = self._data_type_definition.elements_data_size_expression
        namespace = {}
        if context and context.values:
            namespace.update(context.values)
        namespace['__builtins__'] = {}
        try:
            elements_data_size = eval(expression, namespace)
        except Exception as exception:
            raise errors.MappingError(
                'Unable to determine elements data size with error: {0!s}'.
                format(exception))
    if elements_data_size is None or elements_data_size < 0:
        raise errors.MappingError('Invalid elements data size: {0!s}'.
            format(elements_data_size))
    return elements_data_size