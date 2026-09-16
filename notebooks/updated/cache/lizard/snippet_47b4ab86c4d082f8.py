def search_maintenance_window_for_facet(self, facet, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.search_maintenance_window_for_facet_with_http_info(facet,
            **kwargs)
    else:
        data = self.search_maintenance_window_for_facet_with_http_info(facet,
            **kwargs)
        return data