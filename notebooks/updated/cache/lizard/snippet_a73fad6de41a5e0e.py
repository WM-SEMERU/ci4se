def ReadClientLastPings(self, min_last_ping=None, max_last_ping=None,
    fleetspeak_enabled=None):
    last_pings = {}
    for client_id, metadata in iteritems(self.metadatas):
        last_ping = metadata.get('ping', rdfvalue.RDFDatetime(0))
        is_fleetspeak_client = metadata.get('fleetspeak_enabled', False)
        if min_last_ping is not None and last_ping < min_last_ping:
            continue
        elif max_last_ping is not None and last_ping > max_last_ping:
            continue
        elif fleetspeak_enabled is not None and is_fleetspeak_client != fleetspeak_enabled:
            continue
        else:
            last_pings[client_id] = metadata.get('ping', None)
    return last_pings