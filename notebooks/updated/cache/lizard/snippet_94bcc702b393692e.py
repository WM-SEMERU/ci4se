def fetch_by_code(self, code):
    auth_code_data = self.fetchone(self.fetch_code_query, code)
    if auth_code_data is None:
        raise AuthCodeNotFound
    data = dict()
    data_result = self.fetchall(self.fetch_data_query, auth_code_data[0])
    if data_result is not None:
        for dataset in data_result:
            data[dataset[0]] = dataset[1]
    scopes = []
    scope_result = self.fetchall(self.fetch_scopes_query, auth_code_data[0])
    if scope_result is not None:
        for scope_set in scope_result:
            scopes.append(scope_set[0])
    return AuthorizationCode(client_id=auth_code_data[1], code=
        auth_code_data[2], expires_at=auth_code_data[3], redirect_uri=
        auth_code_data[4], scopes=scopes, data=data, user_id=auth_code_data[5])