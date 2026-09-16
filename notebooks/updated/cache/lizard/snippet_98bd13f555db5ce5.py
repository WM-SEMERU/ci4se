def query_raw(self, metric, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.query_raw_with_http_info(metric, **kwargs)
    else:
        data = self.query_raw_with_http_info(metric, **kwargs)
        return data