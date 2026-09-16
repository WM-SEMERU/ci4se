def send(self, path, value, metric_type):
    msg = self._msg_format.format(path=self._build_path(path, metric_type),
        value=value, metric_type=metric_type)
    LOGGER.debug('Sending %s to %s:%s', msg.encode('ascii'), self._host,
        self._port)
    try:
        if self._tcp:
            if self._sock.closed():
                return
            return self._sock.write(msg.encode('ascii'))
        self._sock.sendto(msg.encode('ascii'), (self._host, self._port))
    except iostream.StreamClosedError as error:
        LOGGER.warning('Error sending TCP statsd metric: %s', error)
    except (OSError, socket.error) as error:
        LOGGER.exception('Error sending statsd metric: %s', error)