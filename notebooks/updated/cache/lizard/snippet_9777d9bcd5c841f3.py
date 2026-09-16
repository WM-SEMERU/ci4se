def _on_timeout(self, _attempts=0):
    if self._connection is None and _attempts < 3:
        self._timer = self.session.cluster.connection_class.create_timer(
            0.01, partial(self._on_timeout, _attempts=_attempts + 1))
        return
    if self._connection is not None:
        try:
            self._connection._requests.pop(self._req_id)
        except KeyError:
            return
        pool = self.session._pools.get(self._current_host)
        if pool and not pool.is_shutdown:
            with self._connection.lock:
                self._connection.request_ids.append(self._req_id)
            pool.return_connection(self._connection)
    errors = self._errors
    if not errors:
        if self.is_schema_agreed:
            key = str(self._current_host.endpoint
                ) if self._current_host else 'no host queried before timeout'
            errors = {key:
                'Client request timeout. See Session.execute[_async](timeout)'}
        else:
            connection = self.session.cluster.control_connection._connection
            host = str(connection.endpoint) if connection else 'unknown'
            errors = {host:
                'Request timed out while waiting for schema agreement. See Session.execute[_async](timeout) and Cluster.max_schema_agreement_wait.'
                }
    self._set_final_exception(OperationTimedOut(errors, self._current_host))