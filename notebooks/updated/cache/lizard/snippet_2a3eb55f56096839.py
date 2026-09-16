def create_namespaced_replication_controller(self, namespace, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.create_namespaced_replication_controller_with_http_info(
            namespace, body, **kwargs)
    else:
        data = self.create_namespaced_replication_controller_with_http_info(
            namespace, body, **kwargs)
        return data