def list_pod_disruption_budget_for_all_namespaces(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return (self.
            list_pod_disruption_budget_for_all_namespaces_with_http_info(**
            kwargs))
    else:
        data = (self.
            list_pod_disruption_budget_for_all_namespaces_with_http_info(**
            kwargs))
        return data