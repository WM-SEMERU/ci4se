def encryptParams(self, params, key):
    keypair = Curve.generateKeyPair()
    encodedparams = self.urlencodeParams(params)
    cipher = AESGCM(Curve.calculateAgreement(key, keypair.privateKey))
    ciphertext = cipher.encrypt(b'\x00\x00\x00\x00' + struct.pack('>Q', 0),
        encodedparams.encode(), b'')
    payload = base64.b64encode(keypair.publicKey.serialize()[1:] + ciphertext)
    return [('ENC', payload)]