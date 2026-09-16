def _probe_characteristics_finished(self, result):
    handle = result['context']['handle']
    conn_id = result['context']['connection_id']
    conndata = self._get_connection(handle, 'preparing')
    if conndata is None:
        self._logger.info(
            'Connection disconnected before probe_char... finished, conn_id=%d'
            , conn_id)
        return
    callback = conndata['callback']
    if result['result'] is False:
        conndata['failed'] = True
        conndata['failure_reason'] = 'Could not probe GATT characteristics'
        self.disconnect_async(conn_id, self._on_connection_failed)
        return
    services = result['return_value']['services']
    if TileBusService not in services:
        conndata['failed'] = True
        conndata['failure_reason'
            ] = 'TileBus service not present in GATT services'
        self.disconnect_async(conn_id, self._on_connection_failed)
        return
    conndata['chars_done_time'] = time.time()
    service_time = conndata['services_done_time'] - conndata['connect_time']
    char_time = conndata['chars_done_time'] - conndata['services_done_time']
    total_time = service_time + char_time
    conndata['state'] = 'connected'
    conndata['services'] = services
    conndata['parser'] = IOTileReportParser(report_callback=self._on_report,
        error_callback=self._on_report_error)
    conndata['parser'].context = conn_id
    del conndata['disconnect_handler']
    with self.count_lock:
        self.connecting_count -= 1
    self._logger.info(
        'Total time to connect to device: %.3f (%.3f enumerating services, %.3f enumerating chars)'
        , total_time, service_time, char_time)
    callback(conndata['connection_id'], self.id, True, None)