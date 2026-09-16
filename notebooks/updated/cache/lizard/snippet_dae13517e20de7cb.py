def _format_operation_list(operation, parameters):
    formatted_params = ['?' for _ in parameters]
    try:
        return operation % tuple(formatted_params)
    except TypeError as exc:
        raise exceptions.ProgrammingError(exc)