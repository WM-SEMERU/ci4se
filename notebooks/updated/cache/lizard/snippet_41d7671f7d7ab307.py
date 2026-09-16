def verify_webhook(signature, body):
    public_key = __utils__['http.query']('https://api.travis-ci.org/config')[
        'config']['notifications']['webhook']['public_key']
    pkey_public_key = OpenSSL.crypto.load_publickey(OpenSSL.crypto.
        FILETYPE_PEM, public_key)
    certificate = OpenSSL.crypto.X509()
    certificate.set_pubkey(pkey_public_key)
    signature = base64.b64decode(signature)
    payload = salt.utils.json.loads(parse_qs(body)['payload'][0])
    try:
        OpenSSL.crypto.verify(certificate, signature, payload, six.
            text_type('sha1'))
    except OpenSSL.crypto.Error:
        return False
    return True