def dispatchEvent(self, event, *args):
    for callback in self.listeners[event]:
        yield callback(event, self, *args)