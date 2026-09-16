def connect(self, protocol=None, mode=None, disposition=None):
    CardConnection.connect(self, protocol)
    pcscprotocol = translateprotocolmask(protocol)
    if 0 == pcscprotocol:
        pcscprotocol = self.getProtocol()
    if mode == None:
        mode = SCARD_SHARE_SHARED
    if disposition == None:
        disposition = SCARD_UNPOWER_CARD
    self.disposition = disposition
    hresult, self.hcard, dwActiveProtocol = SCardConnect(self.hcontext, str
        (self.reader), mode, pcscprotocol)
    if hresult != 0:
        self.hcard = None
        if hresult in (SCARD_W_REMOVED_CARD, SCARD_E_NO_SMARTCARD):
            raise NoCardException('Unable to connect', hresult=hresult)
        else:
            raise CardConnectionException(
                'Unable to connect with protocol: ' + dictProtocol[
                pcscprotocol] + '. ' + SCardGetErrorMessage(hresult))
    protocol = 0
    if dwActiveProtocol == SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1:
        protocol = CardConnection.T0_protocol | CardConnection.T1_protocol
    else:
        for p in dictProtocol:
            if p == dwActiveProtocol:
                protocol = eval('CardConnection.%s_protocol' % dictProtocol[p])
    PCSCCardConnection.setProtocol(self, protocol)