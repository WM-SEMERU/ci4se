def refresh_token(token, session=None):
    session = session or HTTP_SESSION
    refresh_data = dict(refresh_token=token.refresh_token, client_id=token.
        consumer_key, client_secret=token.consumer_secret, grant_type=
        'refresh_token')
    resp = session.post(REFRESH_TOKEN_URL, data=refresh_data)
    resp_json = resp.json()
    if 'error' in resp_json:
        message = resp_json['error']
        description = resp_json.get('error_description', '')
        if any(description):
            message = '{}: {}'.format(message, description)
        raise OAuthTokenExpiredError(message)
    return OAuthToken(access_token=resp_json['access_token'], refresh_token
        =token.refresh_token, consumer_key=token.consumer_key,
        consumer_secret=token.consumer_secret)