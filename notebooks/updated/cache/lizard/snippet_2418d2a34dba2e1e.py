def from_app_role(cls, url, path, role_id, secret_id):
    token = cls._fetch_app_role_token(url, role_id, secret_id)
    source_dict = cls._fetch_secrets(url, path, token)
    return cls(source_dict, url, path, token)