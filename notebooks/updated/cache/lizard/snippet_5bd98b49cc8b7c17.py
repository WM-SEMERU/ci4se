def check_password(self, raw_password):
    return xmpp_backend.check_password(self.node, self.domain, raw_password)