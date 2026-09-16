def add_callback(self, callback: callable):

    def internal_callback(*args):
        try:
            callback()
        except TypeError:
            callback(self.get())
    self._var.trace('w', internal_callback)