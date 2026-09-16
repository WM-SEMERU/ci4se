def paginate_query(self, query):
    if self.paginator is None:
        return None
    return self.paginator.paginate_query(query, self.request)