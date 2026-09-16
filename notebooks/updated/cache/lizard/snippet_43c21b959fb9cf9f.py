def make_stanza(self):
    stanza = aioxmpp.Presence()
    self._state.apply_to_stanza(stanza)
    stanza.status.update(self._status)
    return stanza