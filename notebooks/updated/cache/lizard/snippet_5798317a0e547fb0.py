def sort_reverse_chronologically(self):
    self.measurements.sort(key=lambda m: m.timestamp, reverse=True)