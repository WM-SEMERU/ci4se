def reindex(self):
    for i in range(self.count()):
        w = self.points[i]
        w.idx = i
        w.count = self.count()
        w.target_system = self.target_system
        w.target_component = self.target_component
    self.last_change = time.time()