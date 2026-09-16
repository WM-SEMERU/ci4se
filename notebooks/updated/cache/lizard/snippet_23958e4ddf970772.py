def patch_node_status(self, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_node_status_with_http_info(name, body, **kwargs)
    else:
        data = self.patch_node_status_with_http_info(name, body, **kwargs)
        return data