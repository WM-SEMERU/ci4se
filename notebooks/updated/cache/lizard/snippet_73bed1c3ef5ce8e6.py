def open_url(url, headers=None):
    request = urllib2.Request(url)
    if headers:
        for key, value in headers.items():
            request.add_header(key, value)
    return URL_OPENER.open(request)