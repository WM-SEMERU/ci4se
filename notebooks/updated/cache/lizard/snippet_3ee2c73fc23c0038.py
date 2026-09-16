def register(self, observers):
    if isinstance(observers, list) or isinstance(observers, tuple):
        for observer in observers:
            if isinstance(observer, base.Observer):
                self._observers.append(observer)
            else:
                raise InhelitanceError(base.Observer.__name__)
    elif isinstance(observers, base.Observer):
        self._observers.append(observers)