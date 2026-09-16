def write(self, block):
    self.fileobj.write(block)
    self.status.update(len(block))