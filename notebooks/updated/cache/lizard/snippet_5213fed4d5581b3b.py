def get_derived_metric_by_version(self, id, version, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.get_derived_metric_by_version_with_http_info(id,
            version, **kwargs)
    else:
        data = self.get_derived_metric_by_version_with_http_info(id,
            version, **kwargs)
        return data