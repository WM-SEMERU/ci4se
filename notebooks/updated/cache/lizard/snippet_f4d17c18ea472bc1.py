def __conn_listener(self, state):
    if state == KazooState.CONNECTED:
        self.__online = True
        if not self.__connected:
            self.__connected = True
            self._logger.info('Connected to ZooKeeper')
            self._queue.enqueue(self.on_first_connection)
        else:
            self._logger.warning('Re-connected to ZooKeeper')
            self._queue.enqueue(self.on_client_reconnection)
    elif state == KazooState.SUSPENDED:
        self._logger.warning('Connection suspended')
        self.__online = False
    elif state == KazooState.LOST:
        self.__online = False
        self.__connected = False
        if self.__stop:
            self._logger.info('Disconnected from ZooKeeper (requested)')
        else:
            self._logger.warning('Connection lost')