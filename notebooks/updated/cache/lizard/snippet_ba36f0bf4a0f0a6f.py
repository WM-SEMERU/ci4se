def _sha256_sign(self, method, url, headers, body):
    d = ''
    sign_headers = method.upper() + '|' + url + '|'
    for key, value in sorted(headers.items()):
        if key.startswith('X-Mcash-'):
            sign_headers += d + key.upper() + '=' + value
            d = '&'
    rsa_signature = base64.b64encode(self.signer.sign(SHA256.new(sign_headers))
        )
    return 'RSA-SHA256 ' + rsa_signature