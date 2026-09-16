def read_namespaced_persistent_volume_claim_status(self, name, namespace,
    **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return (self.
            read_namespaced_persistent_volume_claim_status_with_http_info(
            name, namespace, **kwargs))
    else:
        data = (self.
            read_namespaced_persistent_volume_claim_status_with_http_info(
            name, namespace, **kwargs))
        return data