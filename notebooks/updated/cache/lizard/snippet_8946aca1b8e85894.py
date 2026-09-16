def handler(self, operation=None, **kwargs):
    response = self._new_response()
    if operation is None:
        response.status = 'error'
        response.error_type = 'MissingOperation'
        response.error_message = 'You must pass an operation'
        return response
    operation = operation.lower()
    self._check_supported_op(operation, response)
    if response.status == 'success':
        method = getattr(self, operation, None)
        if callable(method):
            response = method(**kwargs)
        else:
            response.status == 'error'
            response.error_type = 'NotImplemented'
            msg = 'Operation: {} is not implemented'.format(operation)
            response.error_message = msg
    return response