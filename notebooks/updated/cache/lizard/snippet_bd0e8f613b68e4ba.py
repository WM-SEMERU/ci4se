def post_dissect(self, s):
    if self.tls_session.triggered_prcs_commit:
        if self.tls_session.prcs is not None:
            self.tls_session.rcs = self.tls_session.prcs
            self.tls_session.prcs = None
        self.tls_session.triggered_prcs_commit = False
    if self.tls_session.triggered_pwcs_commit:
        if self.tls_session.pwcs is not None:
            self.tls_session.wcs = self.tls_session.pwcs
            self.tls_session.pwcs = None
        self.tls_session.triggered_pwcs_commit = False
    return s