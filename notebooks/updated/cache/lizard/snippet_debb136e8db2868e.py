def statistics(self):
    result = {}
    for r in self.results:
        result.setdefault(r.status, 0)
        result[r.status] += 1
    return result