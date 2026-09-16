def remove(self, w):
    self.wpoints.remove(w)
    self.last_change = time.time()
    self.reindex()