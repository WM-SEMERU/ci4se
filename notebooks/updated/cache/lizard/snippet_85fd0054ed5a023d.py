def patch_namespaced_custom_object_status(self, group, version, namespace,
    plural, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_namespaced_custom_object_status_with_http_info(group,
            version, namespace, plural, name, body, **kwargs)
    else:
        data = self.patch_namespaced_custom_object_status_with_http_info(group,
            version, namespace, plural, name, body, **kwargs)
        return data