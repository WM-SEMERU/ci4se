def get_node_affiliations(self, jid, node):
    iq = aioxmpp.stanza.IQ(type_=aioxmpp.structs.IQType.GET, to=jid,
        payload=pubsub_xso.OwnerRequest(pubsub_xso.OwnerAffiliations(node)))
    return (yield from self.client.send(iq))