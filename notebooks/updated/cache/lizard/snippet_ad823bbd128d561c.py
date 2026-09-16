def _disconnect(self, handle):
    payload = struct.pack('<B', handle)
    response = self._send_command(3, 0, payload)
    conn_handle, result = unpack('<BH', response.payload)
    if result != 0:
        self._logger.info('Disconnection failed result=%d', result)
        return False, None
    assert conn_handle == handle

    def disconnect_succeeded(event):
        if event.command_class == 3 and event.command == 4:
            event_handle, = unpack('B', event.payload[0:1])
            return event_handle == handle
        return False
    events = self._wait_process_events(3.0, lambda x: False,
        disconnect_succeeded)
    if len(events) != 1:
        return False, None
    return True, {'handle': handle}