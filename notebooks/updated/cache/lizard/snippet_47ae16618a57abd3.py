def read_namespaced_replication_controller_scale(self, name, namespace, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return (self.
            read_namespaced_replication_controller_scale_with_http_info(
            name, namespace, **kwargs))
    else:
        data = (self.
            read_namespaced_replication_controller_scale_with_http_info(
            name, namespace, **kwargs))
        return data