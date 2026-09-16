def get_all_integration_statuses(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.get_all_integration_statuses_with_http_info(**kwargs)
    else:
        data = self.get_all_integration_statuses_with_http_info(**kwargs)
        return data