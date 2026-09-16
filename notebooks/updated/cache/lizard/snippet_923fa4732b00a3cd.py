def _on_trace(_loop, adapter, conn_id, trace):
    conn_string = adapter._get_property(conn_id, 'connection_string')
    if conn_string is None:
        adapter._logger.debug('Dropping trace data with unknown conn_id=%s',
            conn_id)
        return
    adapter.notify_event_nowait(conn_string, 'trace', trace)