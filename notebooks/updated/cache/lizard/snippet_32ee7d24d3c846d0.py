def readShocks(self):
    IndShockConsumerType.readShocks(self)
    self.MrkvNow = self.MrkvNow.astype(int)