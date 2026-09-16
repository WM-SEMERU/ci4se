def connect_all(self):
    if self.__connected:
        return
    with self.__lock:
        for signal in self.__signals:
            self.__connect_signal(signal)
        if self.__slot is not None:
            self.__sigDelayed.connect(self.__slot, Qt.QueuedConnection)
        self.__connected = True