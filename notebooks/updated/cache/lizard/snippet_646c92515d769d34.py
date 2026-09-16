def _is_expired_token_response(cls, response):
    EXPIRED_MESSAGE = 'Expired oauth2 access token'
    INVALID_MESSAGE = 'Invalid oauth2 access token'
    if response.status_code == 400:
        try:
            body = response.json()
            if str(body.get('error_description')) in [EXPIRED_MESSAGE,
                INVALID_MESSAGE]:
                return True
        except:
            pass
    return False