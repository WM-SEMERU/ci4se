def _after_request(self, response):
    cookie_secure = current_app.config['OIDC_COOKIE_SECURE'
        ] and current_app.config.get('OIDC_ID_TOKEN_COOKIE_SECURE', True)
    if getattr(g, 'oidc_id_token_dirty', False):
        if g.oidc_id_token:
            signed_id_token = self.cookie_serializer.dumps(g.oidc_id_token)
            response.set_cookie(current_app.config[
                'OIDC_ID_TOKEN_COOKIE_NAME'], signed_id_token, secure=
                cookie_secure, httponly=True, max_age=current_app.config[
                'OIDC_ID_TOKEN_COOKIE_TTL'])
        else:
            response.set_cookie(current_app.config[
                'OIDC_ID_TOKEN_COOKIE_NAME'], '', path=current_app.config[
                'OIDC_ID_TOKEN_COOKIE_PATH'], secure=cookie_secure,
                httponly=True, expires=0)
    return response