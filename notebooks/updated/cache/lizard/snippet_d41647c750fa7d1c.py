async def _sasl_respond(self):
    if self._sasl_client:
        try:
            response = self._sasl_client.process(self._sasl_challenge)
        except puresasl.SASLError:
            response = None
        if response is None:
            self.logger.warning(
                'SASL challenge processing failed: aborting SASL authentication.'
                )
            await self._sasl_abort()
    else:
        response = b''
    response = base64.b64encode(response).decode(self.encoding)
    to_send = len(response)
    self._sasl_challenge = b''
    while to_send > 0:
        await self.rawmsg('AUTHENTICATE', response[:RESPONSE_LIMIT])
        response = response[RESPONSE_LIMIT:]
        to_send -= RESPONSE_LIMIT
    if to_send == 0:
        await self.rawmsg('AUTHENTICATE', EMPTY_MESSAGE)