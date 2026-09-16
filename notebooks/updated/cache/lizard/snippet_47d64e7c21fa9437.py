def schedule(self, callback, timeout=100):
    timer = QTimer(self)
    timer.timeout.connect(callback)
    timer.start(timeout)
    return timer