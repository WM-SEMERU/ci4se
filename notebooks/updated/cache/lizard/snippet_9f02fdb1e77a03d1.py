def _return_response_and_status_code(response, json_results=True):
    if response.status_code == requests.codes.ok:
        return dict(results=response.json() if json_results else response.
            content, response_code=response.status_code)
    elif response.status_code == 400:
        return dict(error=
            'package sent is either malformed or not within the past 24 hours.'
            , response_code=response.status_code)
    elif response.status_code == 204:
        return dict(error=
            'You exceeded the public API request rate limit (4 requests of any nature per minute)'
            , response_code=response.status_code)
    elif response.status_code == 403:
        return dict(error=
            'You tried to perform calls to functions for which you require a Private API key.'
            , response_code=response.status_code)
    elif response.status_code == 404:
        return dict(error='File not found.', response_code=response.status_code
            )
    else:
        return dict(response_code=response.status_code)