def delete(self):
    res = self.session.delete(self.href)
    self.emit('deleted', self)
    return res