def get_groups_of_apikey(self, api_key, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_groups_of_apikey_with_http_info(api_key, **kwargs)
    else:
        data = self.get_groups_of_apikey_with_http_info(api_key, **kwargs)
        return data