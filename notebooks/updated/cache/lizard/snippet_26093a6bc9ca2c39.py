def error(self):
    if self._error is None:
        try:
            init = getattr(self, '_' + self.__class__.__name__ + '__init', None
                )
            if init is not None and callable(init):
                init()
        except Exception as e:
            pass
    return self._error