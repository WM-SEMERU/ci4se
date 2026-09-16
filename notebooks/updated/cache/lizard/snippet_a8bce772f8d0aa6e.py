def transpose(self, interval, up=True):
    for bar in self.bars:
        bar.transpose(interval, up)
    return self