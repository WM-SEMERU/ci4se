def _StartProcessStatusRPCServer(self):
    if self._rpc_server:
        return
    self._rpc_server = plaso_xmlrpc.XMLProcessStatusRPCServer(self._GetStatus)
    hostname = 'localhost'
    if self._pid < 1024 or self._pid > 60000:
        port = random.randint(1024, 60000)
    else:
        port = self._pid
    if not self._rpc_server.Start(hostname, port):
        port = 0
        for _ in range(self._NUMBER_OF_RPC_SERVER_START_ATTEMPTS):
            port = random.randint(1024, 60000)
            if self._rpc_server.Start(hostname, port):
                break
            port = 0
    if not port:
        logger.error(
            'Unable to start a process status RPC server for {0!s} (PID: {1:d})'
            .format(self._name, self._pid))
        self._rpc_server = None
        return
    self.rpc_port.value = port
    logger.debug('Process: {0!s} process status RPC server started'.format(
        self._name))