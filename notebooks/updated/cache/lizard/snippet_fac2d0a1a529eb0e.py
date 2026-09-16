def sunion(self, *other_sets):
    return self.db.sunion([self.key] + [s.key for s in other_sets])