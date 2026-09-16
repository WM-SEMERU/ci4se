def _expect_response(cls, response, code):
    if response.code != code:
        raise errors.ClientError('Expected {!r} response but got {!r}'.
            format(code, response.code))
    return response