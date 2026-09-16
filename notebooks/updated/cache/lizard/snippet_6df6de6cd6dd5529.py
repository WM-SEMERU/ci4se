def inspect_sensors(self, name=None, timeout=None):
    if name is None:
        msg = katcp.Message.request('sensor-list')
    else:
        msg = katcp.Message.request('sensor-list', name)
    reply, informs = yield self.katcp_client.future_request(msg, timeout=
        timeout)
    self._logger.debug('{} received {} sensor-list informs, reply: {}'.
        format(self.bind_address_string, len(informs), reply))
    if not reply.reply_ok():
        if name is None or 'Unknown sensor' not in reply.arguments[1]:
            raise SyncError('Error reply during sync process: {}'.format(reply)
                )
    sensors_old = set(self._sensors_index.keys())
    sensors_updated = set()
    for msg in informs:
        sen_name = msg.arguments[0]
        sensors_updated.add(sen_name)
        sen = {'description': msg.arguments[1], 'units': msg.arguments[2],
            'sensor_type': msg.arguments[3], 'params': msg.arguments[4:]}
        self._update_index(self._sensors_index, sen_name, sen)
    added, removed = self._difference(sensors_old, sensors_updated, name,
        self._sensors_index)
    for sensor_name in removed:
        if sensor_name in self._sensor_object_cache:
            del self._sensor_object_cache[sensor_name]
    if added or removed:
        raise Return(AttrDict(added=added, removed=removed))