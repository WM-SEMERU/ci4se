def encode(self, pdu):
    if _debug:
        BSLCI._debug('encode %r', pdu)
    PCI.update(pdu, self)
    pdu.put(self.bslciType)
    pdu.put(self.bslciFunction)
    if self.bslciLength != len(self.pduData) + 4:
        raise EncodingError('invalid BSLCI length')
    pdu.put_short(self.bslciLength)