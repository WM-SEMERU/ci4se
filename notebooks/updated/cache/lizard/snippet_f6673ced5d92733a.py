def delete_collection_namespaced_network_policy(self, namespace, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_collection_namespaced_network_policy_with_http_info(
            namespace, **kwargs)
    else:
        data = self.delete_collection_namespaced_network_policy_with_http_info(
            namespace, **kwargs)
        return data