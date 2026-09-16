def build_filters(self, view, filters=None):
    query_builder = self.get_query_builder(backend=self, view=view)
    return query_builder.build_query(**filters if filters else {})