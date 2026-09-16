def list_pre_shared_keys(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.list_pre_shared_keys_with_http_info(**kwargs)
    else:
        data = self.list_pre_shared_keys_with_http_info(**kwargs)
        return data