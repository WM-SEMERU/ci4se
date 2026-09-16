def register(xmlstream, query_xso, timeout=60):
    iq = aioxmpp.IQ(to=aioxmpp.JID.fromstr(xmlstream._to), type_=aioxmpp.
        IQType.SET, payload=query_xso)
    iq.autoset_id()
    yield from aioxmpp.protocol.send_and_wait_for(xmlstream, [iq], [aioxmpp
        .IQ], timeout=timeout)