def connect_post_namespaced_pod_portforward(self, name, namespace, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.connect_post_namespaced_pod_portforward_with_http_info(name
            , namespace, **kwargs)
    else:
        data = self.connect_post_namespaced_pod_portforward_with_http_info(name
            , namespace, **kwargs)
        return data