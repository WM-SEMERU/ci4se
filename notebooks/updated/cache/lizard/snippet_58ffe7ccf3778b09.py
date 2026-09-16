def send_key(self, key, repeat=1):
    for _ in range(repeat):
        self.mediator.send_key(key)
    self.mediator.flush()