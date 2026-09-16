def summaries(self, sc, limit=None):
    clauses = copy(self.clauses)
    schema = self.schema
    if self.prefix:
        schema = ['prefix'] + schema
        clauses['prefix'] = lambda x: True
    with futures.ThreadPoolExecutor(self.max_concurrency) as executor:
        scanned = self._scan(schema, [self.prefix], clauses, executor)
    keys = sc.parallelize(scanned).flatMap(self.store.list_keys)
    return keys.take(limit) if limit else keys.collect()