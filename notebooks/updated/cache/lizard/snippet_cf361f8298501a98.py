def _get_request(url_root, api_key, path, response_type, params, ssl_verify):
    url = _url_builder(url_root, api_key, path, params)
    content = _fetch(url, ssl_verify)
    response = _dispatch(response_type)(content)
    return response