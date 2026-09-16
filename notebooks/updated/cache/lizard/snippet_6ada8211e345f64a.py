def get_groups_of_my_api_key(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_groups_of_my_api_key_with_http_info(**kwargs)
    else:
        data = self.get_groups_of_my_api_key_with_http_info(**kwargs)
        return data