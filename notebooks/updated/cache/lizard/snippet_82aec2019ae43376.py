def listen(self, listen):
    listener = IStreamListener(listen)
    if listener not in self.listeners:
        self.listeners.append(listener)