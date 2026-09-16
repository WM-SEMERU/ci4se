def save(self):
    self.session.add(self)
    self.session.flush()
    return self