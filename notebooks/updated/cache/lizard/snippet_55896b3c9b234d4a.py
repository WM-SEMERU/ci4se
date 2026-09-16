def stop(self):
    self._stopped = True
    threads = [self._accept_thread]
    threads.extend(self._server_threads)
    self._listening_sock.close()
    for sock in list(self._server_socks):
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except socket.error:
            pass
        try:
            sock.close()
        except socket.error:
            pass
    with self._unlock():
        for thread in threads:
            thread.join(10)
    if self._uds_path:
        try:
            os.unlink(self._uds_path)
        except OSError:
            pass