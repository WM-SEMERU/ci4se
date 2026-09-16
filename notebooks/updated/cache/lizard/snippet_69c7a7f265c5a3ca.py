def _check_response(response, expected):
    response_code = response.status_code
    if expected == response_code:
        return
    if response_code < 400:
        raise ex.UnexpectedResponseCodeException(response.text)
    elif response_code == 401:
        raise ex.UnauthorizedException(response.text)
    elif response_code == 400:
        raise ex.BadRequestException(response.text)
    elif response_code == 403:
        raise ex.ForbiddenException(response.text)
    elif response_code == 404:
        raise ex.NotFoundException(response.text)
    elif response_code == 429:
        raise ex.RateLimitedException(response.text)
    else:
        raise ex.InternalServerErrorException(response.text)