def connect_patch_node_proxy_with_path(self, name, path, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.connect_patch_node_proxy_with_path_with_http_info(name,
            path, **kwargs)
    else:
        data = self.connect_patch_node_proxy_with_path_with_http_info(name,
            path, **kwargs)
        return data