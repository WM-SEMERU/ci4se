def run_once(self):
    try:
        if not self._check_connection():
            return 0
    except ChromecastConnectionError:
        return 1
    can_read, _, _ = select.select([self.socket], [], [], self.polltime)
    message = data = None
    if self.socket in can_read and not self._force_recon:
        try:
            message = self._read_message()
        except InterruptLoop as exc:
            if self.stop.is_set():
                self.logger.info(
                    '[%s:%s] Stopped while reading message, disconnecting.',
                    self.fn or self.host, self.port)
            else:
                self.logger.error(
                    '[%s:%s] Interruption caught without being stopped: %s',
                    self.fn or self.host, self.port, exc)
            return 1
        except ssl.SSLError as exc:
            if exc.errno == ssl.SSL_ERROR_EOF:
                if self.stop.is_set():
                    return 1
            raise
        except socket.error:
            self._force_recon = True
            self.logger.error('[%s:%s] Error reading from socket.', self.fn or
                self.host, self.port)
        else:
            data = _json_from_message(message)
    if not message:
        return 0
    if self.stop.is_set():
        return 1
    self._route_message(message, data)
    if REQUEST_ID in data:
        callback = self._request_callbacks.pop(data[REQUEST_ID], None)
        if callback is not None:
            event = callback['event']
            callback['response'] = data
            function = callback['function']
            event.set()
            if function:
                function(data)
    return 0