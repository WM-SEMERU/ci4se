def get_self_url(request_data):
    self_url_host = OneLogin_Saml2_Utils.get_self_url_host(request_data)
    request_uri = ''
    if 'request_uri' in request_data:
        request_uri = request_data['request_uri']
        if not request_uri.startswith('/'):
            match = re.search('^https?://[^/]*(/.*)', request_uri)
            if match is not None:
                request_uri = match.groups()[0]
    return self_url_host + request_uri