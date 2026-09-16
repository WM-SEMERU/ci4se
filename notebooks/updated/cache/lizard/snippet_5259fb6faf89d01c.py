def remember(self, response, request, identity):
    claims = identity.as_dict()
    userid = claims.pop('userid')
    claims_set = self.create_claims_set(request, userid, claims)
    token = self.encode_jwt(claims_set)
    response.headers['Authorization'] = '%s %s' % (self.auth_header_prefix,
        token)