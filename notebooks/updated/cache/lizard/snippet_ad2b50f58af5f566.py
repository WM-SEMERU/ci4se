def get_auth(self):
    auth_resp = get_with_retry(self.cerberus_url + '/v2/auth/user', auth=(
        self.username, self.password), headers=self.HEADERS)
    if auth_resp.status_code != 200:
        throw_if_bad_response(auth_resp)
    return auth_resp.json()