def compute_tls13_next_traffic_secrets(self):
    hkdf = self.prcs.hkdf
    hl = hkdf.hash.digest_size
    cts = self.tls13_derived_secrets['client_traffic_secrets']
    ctsN = cts[-1]
    ctsN_1 = hkdf.expand_label(ctsN, 'application traffic secret', '', hl)
    cts.append(ctsN_1)
    stsN_1 = hkdf.expand_label(ctsN, 'application traffic secret', '', hl)
    cts.append(stsN_1)
    if self.connection_end == 'server':
        self.prcs.tls13_derive_keys(ctsN_1)
        self.pwcs.tls13_derive_keys(stsN_1)
    elif self.connection_end == 'client':
        self.pwcs.tls13_derive_keys(ctsN_1)
        self.prcs.tls13_derive_keys(stsN_1)