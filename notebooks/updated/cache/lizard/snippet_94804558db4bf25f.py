def addObserver(self, observer):
    with self._lock:
        self._weak_observers.append(weakref.ref(observer))
        if len(self._weak_observers) == 1:
            self.startThread()