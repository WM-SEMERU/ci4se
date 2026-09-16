async def client_event_handler(self, client_id, event_tuple, user_data):
    conn_string, event_name, _event = event_tuple
    self._logger.debug(
        'Ignoring event %s from device %s forwarded for client %s',
        event_name, conn_string, client_id)
    return None