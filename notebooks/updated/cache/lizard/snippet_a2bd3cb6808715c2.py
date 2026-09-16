def get_auth_token(self, user_payload):
    username = user_payload.get('username') or None
    password = user_payload.get('password') or None
    if not username or not password:
        raise ValueError(
            '`user_payload` must contain both username and password')
    token = '{username}:{password}'.format(username=username, password=password
        ).encode('utf-8')
    token_b64 = base64.b64encode(token).decode('utf-8', 'ignore')
    return '{auth_header_prefix} {token_b64}'.format(auth_header_prefix=
        self.auth_header_prefix, token_b64=token_b64)