def search_registered_query_for_facets(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.search_registered_query_for_facets_with_http_info(**kwargs)
    else:
        data = self.search_registered_query_for_facets_with_http_info(**kwargs)
        return data