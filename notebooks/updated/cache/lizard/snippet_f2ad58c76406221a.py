def search_tagged_source_for_facets(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.search_tagged_source_for_facets_with_http_info(**kwargs)
    else:
        data = self.search_tagged_source_for_facets_with_http_info(**kwargs)
        return data