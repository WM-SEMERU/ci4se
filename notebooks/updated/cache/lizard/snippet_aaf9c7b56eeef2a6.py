def add_grant(self, grant):
    if hasattr(grant, 'expires_in'):
        self.token_generator.expires_in[grant.grant_type] = grant.expires_in
    if hasattr(grant, 'refresh_expires_in'):
        self.token_generator.refresh_expires_in = grant.refresh_expires_in
    self.grant_types.append(grant)