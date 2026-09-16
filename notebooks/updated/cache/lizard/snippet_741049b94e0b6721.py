def query(self):
    query = self.query_raw
    query = self.authorization.filter_query(query, self)
    query = query.options(*itertools.chain(self.base_query_options, self.
        query_options))
    return query