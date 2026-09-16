def add_loss(self, loss, name=None):
    self.bookkeeper.add_loss(loss, name=name)
    return Loss(self.bookkeeper, tensor=loss, name=name)