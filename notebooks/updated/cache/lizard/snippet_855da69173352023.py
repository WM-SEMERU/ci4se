def pop(self, count=None):
    results = [Job(self.client, **job) for job in json.loads(self.client(
        'pop', self.name, self.worker_name, count or 1))]
    if count is None:
        return len(results) and results[0] or None
    return results