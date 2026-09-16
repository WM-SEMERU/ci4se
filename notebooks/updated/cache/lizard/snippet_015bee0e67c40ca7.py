def reload(self):
    realData = self.load()
    self.clear()
    self.update(realData)