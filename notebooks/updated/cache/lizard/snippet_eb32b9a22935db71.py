def parent(self):
    sub_query = build_query(None)
    query = '^', (self.query, sub_query)
    obj = UIObjectProxy(self.poco)
    obj.query = query
    return obj