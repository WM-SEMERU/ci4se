def _startTimer(self, interval):
    if not self.__timer:
        self.__timer = QtCore.QTimer(self)
        self.__timer.setSingleShot(self.__singleShot)
        self.__timer.setInterval(interval)
        self.__timer.timeout.connect(self.timeout)
        self.__timer.destroyed.connect(self._clearTimer)
        QtCore.QCoreApplication.instance().aboutToQuit.connect(self.__timer
            .stop, QtCore.Qt.QueuedConnection)
    self.__timer.start(interval)