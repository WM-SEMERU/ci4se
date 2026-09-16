def _domain_event_io_error_cb(conn, domain, srcpath, devalias, action,
    reason, opaque):
    _salt_send_domain_event(opaque, conn, domain, opaque['event'], {
        'srcPath': srcpath, 'dev': devalias, 'action':
        _get_libvirt_enum_string('VIR_DOMAIN_EVENT_IO_ERROR_', action),
        'reason': reason})