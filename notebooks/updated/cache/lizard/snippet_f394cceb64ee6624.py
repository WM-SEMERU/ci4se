def compute_tls13_resumption_secret(self):
    if self.connection_end == 'server':
        hkdf = self.prcs.hkdf
    elif self.connection_end == 'client':
        hkdf = self.pwcs.hkdf
    rs = hkdf.derive_secret(self.tls13_master_secret,
        b'resumption master secret', b''.join(self.handshake_messages))
    self.tls13_derived_secrets['resumption_secret'] = rs