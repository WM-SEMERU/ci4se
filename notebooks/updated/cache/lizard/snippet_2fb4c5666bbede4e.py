def calculateSignature(privateSigningKey, message):
    if privateSigningKey.getType() == Curve.DJB_TYPE:
        rand = os.urandom(64)
        res = _curve.calculateSignature(rand, privateSigningKey.
            getPrivateKey(), message)
        return res
    else:
        raise InvalidKeyException('Unknown type: %s' % privateSigningKey.
            getType())