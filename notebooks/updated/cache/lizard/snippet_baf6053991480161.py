def peek(self, count=None):
    results = [Job(self.client, **rec) for rec in json.loads(self.client(
        'peek', self.name, count or 1))]
    if count is None:
        return len(results) and results[0] or None
    return results