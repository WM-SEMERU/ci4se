def url_for(self, attr=None, filter_value=None, service_type=None,
    endpoint_type='publicURL', service_name=None, volume_service_name=None):
    matching_endpoints = []
    if 'serviceCatalog' not in self.catalog['access']:
        return None
    catalog = self.catalog['access']['serviceCatalog']
    for service in catalog:
        if service.get('type') != service_type:
            continue
        endpoints = service['endpoints']
        for endpoint in endpoints:
            if not filter_value or endpoint.get(attr) == filter_value:
                endpoint['serviceName'] = service.get('name')
                matching_endpoints.append(endpoint)
    if not matching_endpoints:
        raise exc.EndpointNotFound()
    elif len(matching_endpoints) > 1:
        raise exc.AmbiguousEndpoints(endpoints=matching_endpoints)
    else:
        return matching_endpoints[0][endpoint_type]