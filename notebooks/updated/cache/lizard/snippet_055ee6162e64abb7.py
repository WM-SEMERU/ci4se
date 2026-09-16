def create_app(client_name, scopes=__DEFAULT_SCOPES, redirect_uris=None,
    website=None, to_file=None, api_base_url=__DEFAULT_BASE_URL,
    request_timeout=__DEFAULT_TIMEOUT, session=None):
    api_base_url = Mastodon.__protocolize(api_base_url)
    request_data = {'client_name': client_name, 'scopes': ' '.join(scopes)}
    try:
        if redirect_uris is not None:
            if isinstance(redirect_uris, (list, tuple)):
                redirect_uris = '\n'.join(list(redirect_uris))
            request_data['redirect_uris'] = redirect_uris
        else:
            request_data['redirect_uris'] = 'urn:ietf:wg:oauth:2.0:oob'
        if website is not None:
            request_data['website'] = website
        if session:
            ret = session.post(api_base_url + '/api/v1/apps', data=
                request_data, timeout=request_timeout)
            response = ret.json()
        else:
            response = requests.post(api_base_url + '/api/v1/apps', data=
                request_data, timeout=request_timeout)
            response = response.json()
    except Exception as e:
        raise MastodonNetworkError('Could not complete request: %s' % e)
    if to_file is not None:
        with open(to_file, 'w') as secret_file:
            secret_file.write(response['client_id'] + '\n')
            secret_file.write(response['client_secret'] + '\n')
    return response['client_id'], response['client_secret']