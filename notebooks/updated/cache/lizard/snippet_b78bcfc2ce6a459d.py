def disconnect(self):
    if self.root.ref is not None:
        self.api.disconnect()
    self.root = None