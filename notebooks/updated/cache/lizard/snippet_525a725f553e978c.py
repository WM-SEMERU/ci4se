def _validate_operator_name(operator, supported_operators):
    if not isinstance(operator, six.text_type):
        raise TypeError('Expected operator as unicode string, got: {} {}'.
            format(type(operator).__name__, operator))
    if operator not in supported_operators:
        raise GraphQLCompilationError('Unrecognized operator: {}'.format(
            operator))