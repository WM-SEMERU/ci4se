def connect_head_namespaced_pod_proxy_with_path(self, name, namespace, path,
    **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.connect_head_namespaced_pod_proxy_with_path_with_http_info(
            name, namespace, path, **kwargs)
    else:
        data = self.connect_head_namespaced_pod_proxy_with_path_with_http_info(
            name, namespace, path, **kwargs)
        return data