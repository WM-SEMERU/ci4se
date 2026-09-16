def patch_namespace(self, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_namespace_with_http_info(name, body, **kwargs)
    else:
        data = self.patch_namespace_with_http_info(name, body, **kwargs)
        return data