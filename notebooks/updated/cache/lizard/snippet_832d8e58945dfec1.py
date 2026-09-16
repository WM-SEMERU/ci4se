def on_message(self, name):

    def decorator(fn):
        if isinstance(name, list):
            for n in name:
                self.add_message_listener(n, fn)
        else:
            self.add_message_listener(name, fn)
    return decorator