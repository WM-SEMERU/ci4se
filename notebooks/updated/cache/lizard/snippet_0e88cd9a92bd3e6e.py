def register(self):
    if not self.registered:
        self.registered = True
        if self.parent:
            self.parent.register(self)