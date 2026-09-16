async def on_raw_cap_ack(self, params):
    for capab in params[0].split():
        cp, value = self._capability_normalize(capab)
        self._capabilities_requested.discard(cp)
        if capab.startswith(DISABLED_PREFIX):
            self._capabilities[cp] = False
            attr = 'on_capability_' + pydle.protocol.identifierify(cp
                ) + '_disabled'
        elif capab.startswith(STICKY_PREFIX):
            self.logger.error('Could not disable capability %s.', cp)
            continue
        else:
            self._capabilities[cp] = value if value else True
            attr = 'on_capability_' + pydle.protocol.identifierify(cp
                ) + '_enabled'
        if capab.startswith(ACKNOWLEDGEMENT_REQUIRED_PREFIX):
            await self.rawmsg('CAP', 'ACK', cp)
        if hasattr(self, attr):
            status = await getattr(self, attr)()
        else:
            status = NEGOTIATED
        if status == NEGOTIATING:
            self._capabilities_negotiating.add(cp)
        elif status == FAILED:
            self.logger.warning(
                'Capability negotiation for %s failed. Attempting to disable capability again.'
                , cp)
            await self.rawmsg('CAP', 'REQ', '-' + cp)
            self._capabilities_requested.add(cp)
    if not self._capabilities_requested and not self._capabilities_negotiating:
        await self.rawmsg('CAP', 'END')