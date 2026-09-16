def _salt_send_domain_event(opaque, conn, domain, event, event_data):
    data = {'domain': {'name': domain.name(), 'id': domain.ID(), 'uuid':
        domain.UUIDString()}, 'event': event}
    data.update(event_data)
    _salt_send_event(opaque, conn, data)