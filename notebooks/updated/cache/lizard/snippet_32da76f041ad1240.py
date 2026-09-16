def _receive(self):
    data_in = EMPTY_BUFFER
    try:
        data_in = self._read_from_socket()
    except socket.timeout:
        pass
    except (IOError, OSError) as why:
        if why.args[0] not in (EWOULDBLOCK, EAGAIN):
            self._exceptions.append(AMQPConnectionError(why))
            self._running.clear()
    return data_in