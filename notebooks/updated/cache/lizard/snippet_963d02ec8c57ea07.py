def query_certificate(self, cert_hash):
    try:
        cquery = self.pssl.query_cert(cert_hash)
    except Exception:
        self.error(
            'Exception during processing with passiveSSL. This happens if the given hash is not sha1 or contains dashes/colons etc. Please make sure to submit a clean formatted sha1 hash.'
            )
    try:
        cfetch = self.pssl.fetch_cert(cert_hash, make_datetime=False)
    except Exception:
        cfetch = {}
    return {'query': cquery, 'cert': cfetch}