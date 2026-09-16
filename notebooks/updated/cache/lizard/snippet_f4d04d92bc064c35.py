def replace_namespaced_ingress(self, name, namespace, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.replace_namespaced_ingress_with_http_info(name,
            namespace, body, **kwargs)
    else:
        data = self.replace_namespaced_ingress_with_http_info(name,
            namespace, body, **kwargs)
        return data