def get_request(request_url, request_headers=dict()):
    request = Request(request_url)
    for key, val in request_headers.items():
        request.add_header(key, val)
    try:
        response = urlopen(request, timeout=_REQUEST_TIMEOUT)
        response_content = response.read()
    except (HTTPError, URLError, socket.timeout):
        response_content = None
    return response_content