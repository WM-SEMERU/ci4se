def progress_stats(self, id):
    schema = ProgressSchema()
    resp = self.service.get(self.base + str(id) + '/', params={'stats':
        'progress'})
    return self.service.decode(schema, resp)