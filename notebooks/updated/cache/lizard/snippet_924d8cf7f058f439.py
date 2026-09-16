def delete_namespaced_controller_revision(self, name, namespace, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_namespaced_controller_revision_with_http_info(name,
            namespace, **kwargs)
    else:
        data = self.delete_namespaced_controller_revision_with_http_info(name,
            namespace, **kwargs)
        return data