def get_secret_versions(self, secure_data_path, limit=None, offset=None):
    if not limit or limit <= 0:
        limit = 100
    if not offset or offset < 0:
        offset = 0
    payload = {'limit': str(limit), 'offset': str(offset)}
    secret_resp = get_with_retry(str.join('', [self.cerberus_url,
        '/v1/secret-versions/', secure_data_path]), params=payload, headers
        =self.HEADERS)
    throw_if_bad_response(secret_resp)
    return secret_resp.json()