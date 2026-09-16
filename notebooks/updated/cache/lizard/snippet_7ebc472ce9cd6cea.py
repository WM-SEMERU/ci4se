def patch_audit_sink(self, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_audit_sink_with_http_info(name, body, **kwargs)
    else:
        data = self.patch_audit_sink_with_http_info(name, body, **kwargs)
        return data