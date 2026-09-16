def servers_update_addresses(request, servers, all_tenants=False):
    neutron_enabled = base.is_service_enabled(request, 'network')
    if neutron_enabled:
        neutron.servers_update_addresses(request, servers, all_tenants)