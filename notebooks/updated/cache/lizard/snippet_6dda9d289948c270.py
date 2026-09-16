def write(self, message, cur_time=None):
    if cur_time is None:
        cur_time = time.time()
    lines = self._line_buffer.add_string(message)
    for line in lines:
        timestamp = ''
        if self._prepend_timestamp:
            timestamp = datetime.datetime.utcfromtimestamp(cur_time).isoformat(
                ) + ' '
        line = '{}{}{}'.format(self._line_prepend, timestamp, line)
        self._fsapi.push(self._filename, line)