def from_response(response):
    if response.code:
        return ERRORS[response.code](response)
    else:
        return Error(response)