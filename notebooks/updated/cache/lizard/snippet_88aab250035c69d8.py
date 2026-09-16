def unlisten(self, event, callback):
    try:
        self.listeners[event].remove(callback)
    except ValueError:
        return False
    else:
        return True