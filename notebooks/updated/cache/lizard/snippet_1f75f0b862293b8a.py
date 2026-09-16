def _set_ciphers(self):
    ciphers = (Security.SSLCipherSuite * len(CIPHER_SUITES))(*CIPHER_SUITES)
    result = Security.SSLSetEnabledCiphers(self.context, ciphers, len(
        CIPHER_SUITES))
    _assert_no_error(result)