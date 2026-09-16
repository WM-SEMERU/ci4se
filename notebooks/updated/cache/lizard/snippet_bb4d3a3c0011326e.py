def patch_namespaced_pod_disruption_budget(self, name, namespace, body, **
    kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.patch_namespaced_pod_disruption_budget_with_http_info(name,
            namespace, body, **kwargs)
    else:
        data = self.patch_namespaced_pod_disruption_budget_with_http_info(name,
            namespace, body, **kwargs)
        return data