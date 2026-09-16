def _perform_validation(self, path, value, results):
    name = path if path != None else 'value'
    value = ObjectReader.get_value(value)
    super(ArraySchema, self)._perform_validation(path, value, results)
    if value == None:
        return
    if isinstance(value, list) or isinstance(value, set) or isinstance(value,
        tuple):
        index = 0
        for element in value:
            element_path = str(index) if path == None or len(path
                ) == 0 else path + '.' + str(index)
            self._perform_type_validation(element_path, self.value_type,
                element, results)
            index += 1
    else:
        results.append(ValidationResult(path, ValidationResultType.Error,
            'VALUE_ISNOT_ARRAY', name + ' type must be List or Array',
            'List', type(value)))