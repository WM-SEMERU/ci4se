def compute(self):
    if 'Signature' in self.params:
        raise RuntimeError('Existing signature in parameters')
    if self.signature_version is not None:
        version = self.signature_version
    else:
        version = self.params['SignatureVersion']
    if str(version) == '1':
        bytes = self.old_signing_text()
        hash_type = 'sha1'
    elif str(version) == '2':
        bytes = self.signing_text()
        if self.signature_method is not None:
            signature_method = self.signature_method
        else:
            signature_method = self.params['SignatureMethod']
        hash_type = signature_method[len('Hmac'):].lower()
    else:
        raise RuntimeError("Unsupported SignatureVersion: '%s'" % version)
    return self.creds.sign(bytes, hash_type)