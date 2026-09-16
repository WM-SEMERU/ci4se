def parse_response(cls, response, **kwargs):
    if response.tag != cls.command_name:
        raise ResponseParseError(
            'Received response of type {}, PutCommand can only parse responses of type {}'
            .format(response.tag, cls.command_name))
    error = response.find('./error')
    if error is not None:
        return _parse_error_tree(error)
    return None