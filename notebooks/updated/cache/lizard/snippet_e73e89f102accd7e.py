def _reconnect_internal(self):
    errors = {}
    lbp = (self._cluster.load_balancing_policy if self._cluster.
        _config_mode == _ConfigMode.LEGACY else self._cluster.
        _default_load_balancing_policy)
    for host in lbp.make_query_plan():
        try:
            return self._try_connect(host)
        except ConnectionException as exc:
            errors[str(host.endpoint)] = exc
            log.warning('[control connection] Error connecting to %s:',
                host, exc_info=True)
            self._cluster.signal_connection_failure(host, exc,
                is_host_addition=False)
        except Exception as exc:
            errors[str(host.endpoint)] = exc
            log.warning('[control connection] Error connecting to %s:',
                host, exc_info=True)
        if self._is_shutdown:
            raise DriverException(
                '[control connection] Reconnection in progress during shutdown'
                )
    raise NoHostAvailable('Unable to connect to any servers', errors)