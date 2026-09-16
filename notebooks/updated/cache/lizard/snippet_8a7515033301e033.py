def get(self, **options):
    sub_query = self.with_limit(1)
    options = QueryOptions(sub_query).replace(batch_size=1)
    for result in sub_query.run(**options):
        return result
    return None