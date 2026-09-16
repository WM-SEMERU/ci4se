def delete_cluster_role_binding(self, name, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_cluster_role_binding_with_http_info(name, **kwargs)
    else:
        data = self.delete_cluster_role_binding_with_http_info(name, **kwargs)
        return data