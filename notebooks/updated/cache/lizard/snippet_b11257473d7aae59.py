def error_response(response):
    if response.status_code >= 500:
        raise exceptions.GeocodioServerError
    elif response.status_code == 403:
        raise exceptions.GeocodioAuthError
    elif response.status_code == 422:
        raise exceptions.GeocodioDataError(response.json()['error'])
    else:
        raise exceptions.GeocodioError('Unknown service error (HTTP {0})'.
            format(response.status_code))