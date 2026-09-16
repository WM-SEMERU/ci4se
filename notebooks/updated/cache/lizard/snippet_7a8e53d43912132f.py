def _get_api_key_ops():
    auth_header = request.authorization
    if not auth_header:
        logging.debug('API request lacks authorization header')
        abort(flask.Response('API key required', 401, {'WWW-Authenticate':
            'Basic realm="API key required"'}))
    return operations.ApiKeyOps(auth_header.username, auth_header.password)