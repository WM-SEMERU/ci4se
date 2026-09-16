def SignMessage(self, message, script_hash):
    keypair = self.GetKeyByScriptHash(script_hash)
    prikey = bytes(keypair.PrivateKey)
    res = Crypto.Default().Sign(message, prikey)
    return res, keypair.PublicKey