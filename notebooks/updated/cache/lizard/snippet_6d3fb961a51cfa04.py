def signMsg(self, msg: Dict, identifier: Identifier=None, otherIdentifier:
    Identifier=None):
    idr = self.requiredIdr(idr=identifier or otherIdentifier)
    signer = self._signerById(idr)
    signature = signer.sign(msg)
    return signature