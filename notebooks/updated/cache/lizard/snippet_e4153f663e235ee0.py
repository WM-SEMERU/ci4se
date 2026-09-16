def flush_events(self):
    response = self._send_data('DELETE', 'admin', 'flush-events', {})
    if response['success']:
        msg = 'Events flushed'
    else:
        msg = 'Flushing of events failed'
    output = {'message': msg}
    return output