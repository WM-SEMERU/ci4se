def getpeercert(self, binary_form=False):
    try:
        peer_cert = _X509(SSL_get_peer_certificate(self._ssl.value))
    except openssl_error():
        return
    if binary_form:
        return i2d_X509(peer_cert.value)
    if self._cert_reqs == CERT_NONE:
        return {}
    return decode_cert(peer_cert)