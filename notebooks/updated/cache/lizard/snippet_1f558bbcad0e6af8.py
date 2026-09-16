def list_api_service(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.list_api_service_with_http_info(**kwargs)
    else:
        data = self.list_api_service_with_http_info(**kwargs)
        return data