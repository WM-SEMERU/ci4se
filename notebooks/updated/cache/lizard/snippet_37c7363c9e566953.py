def InternalSendApdu(self, apdu_to_send):
    response = None
    if not self.use_legacy_format:
        response = apdu.ResponseApdu(self.transport.SendMsgBytes(
            apdu_to_send.ToByteArray()))
        if response.sw1 == 103 and response.sw2 == 0:
            self.use_legacy_format = True
            return self.InternalSendApdu(apdu_to_send)
    else:
        response = apdu.ResponseApdu(self.transport.SendMsgBytes(
            apdu_to_send.ToLegacyU2FByteArray()))
    return response