def verify(self, msg, signature, key):
    try:
        key.verify(signature, msg, padding.PSS(mgf=padding.MGF1(self.
            hash_algorithm()), salt_length=padding.PSS.MAX_LENGTH), self.
            hash_algorithm())
    except InvalidSignature as err:
        raise BadSignature(err)
    else:
        return True