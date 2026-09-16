def encrypt(self, msg, pubkey, enhex=False):
    if not isinstance(pubkey, PublicKey):
        if len(pubkey) == 32:
            pubkey = PublicKey(pubkey, encoding.RawEncoder)
        else:
            pubkey = PublicKey(pubkey, encoding.HexEncoder)
    box = Box(self.key, pubkey)
    nonce = self.nonce()
    encoder = encoding.HexEncoder if enhex else encoding.RawEncoder
    encrypted = box.encrypt(msg, nonce, encoder)
    return encrypted.ciphertext, encrypted.nonce