def remove_listener(self, callback):
    listeners = filter(lambda x: x['callback'] == callback, self.listeners)
    for l in listeners:
        self.listeners.remove(l)