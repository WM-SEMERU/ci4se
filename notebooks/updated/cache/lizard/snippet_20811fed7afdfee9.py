def tls_session_update(self, msg_str):
    super(TLSClientHello, self).tls_session_update(msg_str)
    self.tls_session.advertised_tls_version = self.version
    self.random_bytes = msg_str[10:38]
    self.tls_session.client_random = struct.pack('!I', self.gmt_unix_time
        ) + self.random_bytes
    if self.ext:
        for e in self.ext:
            if isinstance(e, TLS_Ext_SupportedVersions):
                if self.tls_session.tls13_early_secret is None:
                    self.tls_session.compute_tls13_early_secrets()
                break