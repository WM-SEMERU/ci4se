def _send_stanza(self, xmlstream, token):
    if token.state == StanzaState.ABORTED:
        return
    stanza_obj = token.stanza
    if isinstance(stanza_obj, stanza.Presence):
        stanza_obj = self.app_outbound_presence_filter.filter(stanza_obj)
        if stanza_obj is not None:
            stanza_obj = self.service_outbound_presence_filter.filter(
                stanza_obj)
    elif isinstance(stanza_obj, stanza.Message):
        stanza_obj = self.app_outbound_message_filter.filter(stanza_obj)
        if stanza_obj is not None:
            stanza_obj = self.service_outbound_message_filter.filter(stanza_obj
                )
    if stanza_obj is None:
        token._set_state(StanzaState.DROPPED)
        self._logger.debug('outgoing stanza %r dropped by filter chain',
            token.stanza)
        return
    self._logger.debug('forwarding stanza to xmlstream: %r', stanza_obj)
    try:
        xmlstream.send_xso(stanza_obj)
    except Exception as exc:
        self._logger.warning('failed to send stanza', exc_info=True)
        token._set_state(StanzaState.FAILED, exc)
        return
    if self._sm_enabled:
        token._set_state(StanzaState.SENT)
        self._sm_unacked_list.append(token)
    else:
        token._set_state(StanzaState.SENT_WITHOUT_SM)