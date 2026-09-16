def service_confirmation(self, conn, bslpdu):
    if _debug:
        ProxyServerService._debug('service_confirmation %r %r', conn, bslpdu)
    if not getattr(conn, 'proxyAdapter', None):
        raise RuntimeError(
            'service confirmation received but no adapter for it')
    conn.proxyAdapter.service_confirmation(bslpdu)