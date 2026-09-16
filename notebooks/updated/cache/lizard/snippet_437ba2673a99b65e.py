def verify_oauth2_token(id_token, request, audience=None):
    return verify_token(id_token, request, audience=audience, certs_url=
        _GOOGLE_OAUTH2_CERTS_URL)