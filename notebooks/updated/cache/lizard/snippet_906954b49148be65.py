def _on_scan(_loop, adapter, _adapter_id, info, expiration_time):
    info['validity_period'] = expiration_time
    adapter.notify_event_nowait(info.get('connection_string'),
        'device_seen', info)