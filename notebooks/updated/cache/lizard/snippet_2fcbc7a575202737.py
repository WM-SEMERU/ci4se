def set_format(self, column_or_columns, formatter):
    if inspect.isclass(formatter):
        formatter = formatter()
    if callable(formatter) and not hasattr(formatter, 'format_column'):
        formatter = _formats.FunctionFormatter(formatter)
    if not hasattr(formatter, 'format_column'):
        raise Exception('Expected Formatter or function: ' + str(formatter))
    for label in self._as_labels(column_or_columns):
        if formatter.converts_values:
            self[label] = formatter.convert_column(self[label])
        self._formats[label] = formatter
    return self