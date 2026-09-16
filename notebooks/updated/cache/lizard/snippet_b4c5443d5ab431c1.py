def loop_read(self, max_packets=1):
    if self._sock is None and self._ssl is None:
        return MQTT_ERR_NO_CONN
    max_packets = len(self._out_messages) + len(self._in_messages)
    if max_packets < 1:
        max_packets = 1
    for i in range(0, max_packets):
        rc = self._packet_read()
        if rc > 0:
            return self._loop_rc_handle(rc)
        elif rc == MQTT_ERR_AGAIN:
            return MQTT_ERR_SUCCESS
    return MQTT_ERR_SUCCESS