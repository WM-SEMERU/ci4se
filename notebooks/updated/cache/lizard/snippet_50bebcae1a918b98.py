def delete_derived_metric(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_derived_metric_with_http_info(id, **kwargs)
    else:
        data = self.delete_derived_metric_with_http_info(id, **kwargs)
        return data