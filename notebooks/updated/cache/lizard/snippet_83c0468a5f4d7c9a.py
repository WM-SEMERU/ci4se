def patch_namespaced_daemon_set(self, name, namespace, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_namespaced_daemon_set_with_http_info(name,
            namespace, body, **kwargs)
    else:
        data = self.patch_namespaced_daemon_set_with_http_info(name,
            namespace, body, **kwargs)
        return data