def _pool_event_lifecycle_cb(conn, pool, event, detail, opaque):
    _salt_send_event(opaque, conn, {'pool': {'name': pool.name(), 'uuid':
        pool.UUIDString()}, 'event': _get_libvirt_enum_string(
        'VIR_STORAGE_POOL_EVENT_', event), 'detail': 'unknown'})