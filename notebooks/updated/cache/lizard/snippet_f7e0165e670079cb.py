def _on_trace(self, sequence, topic, message):
    try:
        conn_key = self._find_connection(topic)
        conn_id = self.conns.get_connection_id(conn_key)
    except ArgumentError:
        self._logger.warn(
            'Dropping trace message that does not correspond with a known connection, topic=%s'
            , topic)
        return
    try:
        tracing = messages.TracingNotification.verify(message)
        self._trigger_callback('on_trace', conn_id, tracing['trace'])
    except Exception:
        self._logger.exception('Error processing trace conn_id=%d', conn_id)