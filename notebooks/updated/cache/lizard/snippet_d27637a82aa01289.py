def get_network_create_endpoint_kwargs(self, action, endpoint_config,
    kwargs=None):
    map_name = action.config_id.map_name
    policy = self._policy
    c_kwargs = dict(ipv4_address=resolve_value(endpoint_config.ipv4_address
        ), ipv6_address=resolve_value(endpoint_config.ipv6_address))
    if endpoint_config.aliases:
        c_kwargs['aliases'] = list(map(resolve_value, endpoint_config.aliases))
    if endpoint_config.links:
        c_kwargs['links'] = [(policy.cname(map_name, l_name), alias or
            policy.get_hostname(l_name)) for l_name, alias in
            endpoint_config.links]
    if endpoint_config.link_local_ips:
        c_kwargs['link_local_ips'] = list(map(resolve_value,
            endpoint_config.link_local_ips))
    update_kwargs(c_kwargs, kwargs)
    return c_kwargs