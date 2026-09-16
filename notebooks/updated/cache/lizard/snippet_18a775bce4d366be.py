def VerifyGitkitToken(self, jwt):
    certs = self.rpc_helper.GetPublicCert()
    crypt.MAX_TOKEN_LIFETIME_SECS = 30 * 86400
    parsed = None
    for aud in filter(lambda x: x is not None, [self.project_id, self.
        client_id]):
        try:
            parsed = crypt.verify_signed_jwt_with_certs(jwt, certs, aud)
        except crypt.AppIdentityError as e:
            if 'Wrong recipient' not in e.message:
                return None
        if parsed:
            return GitkitUser.FromToken(parsed)
    return None