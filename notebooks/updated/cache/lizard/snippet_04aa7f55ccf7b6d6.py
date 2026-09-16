def _handle_error(response):
    code = response.status_code
    if 200 <= code < 400:
        return
    if code == 400:
        sys.stderr.write(response.text + '\n')
        raise BadRequest(response)
    elif code == 401:
        sys.stderr.write(response.text + '\n')
        raise UnauthorizedAccess(response)
    elif code == 403:
        sys.stderr.write(response.text + '\n')
        raise ForbiddenAccess(response)
    elif code == 404:
        sys.stderr.write(response.text + '\n')
        raise ResourceNotFound(response)
    elif code == 405:
        sys.stderr.write(response.text + '\n')
        raise MethodNotAllowed(response)
    elif code == 409:
        sys.stderr.write(response.text + '\n')
        raise ResourceConflict(response)
    elif code == 422:
        sys.stderr.write(response.text + '\n')
        raise ResourceInvalid(response)
    elif code in (449, 502, 503, 504):
        sys.stderr.write(response.text + '\n')
        raise RetryWithDelay(response)
    elif 401 <= code < 500:
        sys.stderr.write(response.text + '\n')
        raise ClientError(response)
    elif 500 <= code < 600:
        sys.stderr.write(response.text + '\n')
        raise ServerError(response)
    else:
        raise ConnectionError(response)