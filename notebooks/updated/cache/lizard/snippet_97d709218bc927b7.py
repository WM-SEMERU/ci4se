def device_query_retrieve(self, query_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.device_query_retrieve_with_http_info(query_id, **kwargs)
    else:
        data = self.device_query_retrieve_with_http_info(query_id, **kwargs)
        return data