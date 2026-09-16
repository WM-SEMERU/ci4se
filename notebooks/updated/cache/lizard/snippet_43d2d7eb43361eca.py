def get_meta(self, **kwargs):
    query = kwargs
    query = query_params(query, 'productid', None, short_hand='pid')
    query = query_params(query, 'query', 'product')
    query = query_params(query, 'results', 'm')
    query = query_params(query, 'output', 'j')
    return query_ode(self.ode_url, query=query)