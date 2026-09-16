def _create_session(team, auth):
    session = requests.Session()
    session.hooks.update(dict(response=partial(_handle_response, team)))
    session.headers.update({'Content-Type': 'application/json', 'Accept':
        'application/json', 'User-Agent': 'quilt-cli/%s (%s %s) %s/%s' % (
        VERSION, platform.system(), platform.release(), platform.
        python_implementation(), platform.python_version())})
    if auth is not None:
        session.headers['Authorization'] = 'Bearer %s' % auth['access_token']
    return session