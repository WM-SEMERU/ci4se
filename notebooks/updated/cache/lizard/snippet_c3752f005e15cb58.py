def should_add_ClientCertificate(self):
    hs_msg = [type(m) for m in self.cur_session.handshake_messages_parsed]
    if TLSCertificateRequest not in hs_msg:
        return
    certs = []
    if self.mycert:
        certs = [self.mycert]
    self.add_msg(TLSCertificate(certs=certs))
    raise self.ADDED_CLIENTCERTIFICATE()