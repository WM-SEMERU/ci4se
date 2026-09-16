def subscribe(self, peer_jid):
    self.client.enqueue(stanza.Presence(type_=structs.PresenceType.
        SUBSCRIBE, to=peer_jid))