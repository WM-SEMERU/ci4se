def find(self, query, threshold=None):
    results = self.search(query, threshold)
    if results:
        return results[0][0]
    else:
        return None