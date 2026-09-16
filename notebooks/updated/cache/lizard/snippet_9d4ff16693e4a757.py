def _domain_event_tray_change_cb(conn, domain, dev, reason, opaque):
    _salt_send_domain_event(opaque, conn, domain, opaque['event'], {'dev':
        dev, 'reason': _get_libvirt_enum_string(
        'VIR_DOMAIN_EVENT_TRAY_CHANGE_', reason)})