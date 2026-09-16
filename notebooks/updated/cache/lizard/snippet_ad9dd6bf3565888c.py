def _find_func(self, operation):
    if isinstance(operation, Operation):
        operation_name = operation.name.lower()
    else:
        operation_name = operation.lower()
    return getattr(self, 'configure_{}'.format(operation_name))