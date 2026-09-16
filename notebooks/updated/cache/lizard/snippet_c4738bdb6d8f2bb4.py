def full(self):
    return self.maxsize and len(self.list) >= self.maxsize or False