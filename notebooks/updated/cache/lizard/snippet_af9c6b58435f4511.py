def send_is_typing(self, peer_jid: str, is_typing: bool):
    if self.is_group_jid(peer_jid):
        return self._send_xmpp_element(chatting.OutgoingGroupIsTypingEvent(
            peer_jid, is_typing))
    else:
        return self._send_xmpp_element(chatting.OutgoingIsTypingEvent(
            peer_jid, is_typing))