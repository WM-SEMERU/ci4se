def delete_namespaced_pod_template(self, name, namespace, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_namespaced_pod_template_with_http_info(name,
            namespace, **kwargs)
    else:
        data = self.delete_namespaced_pod_template_with_http_info(name,
            namespace, **kwargs)
        return data