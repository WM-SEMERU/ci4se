def __callHandler(self, callback, event, *params):
    if callback is not None:
        event.hook = self
        callback(event, *params)