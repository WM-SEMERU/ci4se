def append(self, event, category=None):
    date = datetime.datetime.now()
    self.store.insert(0, (date, event, category))
    if len(self.store) > self.size:
        del self.store[-1]