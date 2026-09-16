def set_node_config(self, jid, config, node=None):
    iq = aioxmpp.stanza.IQ(to=jid, type_=aioxmpp.structs.IQType.SET)
    iq.payload = pubsub_xso.OwnerRequest(pubsub_xso.OwnerConfigure(node=node))
    iq.payload.payload.data = config
    yield from self.client.send(iq)