def create_external_link(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.create_external_link_with_http_info(**kwargs)
    else:
        data = self.create_external_link_with_http_info(**kwargs)
        return data