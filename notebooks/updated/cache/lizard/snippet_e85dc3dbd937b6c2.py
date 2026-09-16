def network_create_notif(self, tenant_id, tenant_name, cidr):
    router_id = self.get_router_id(tenant_id, tenant_name)
    if not router_id:
        LOG.error('Rout ID not present for tenant')
        return False
    ret = self._program_dcnm_static_route(tenant_id, tenant_name)
    if not ret:
        LOG.error('Program DCNM with static routes failed for router %s',
            router_id)
        return False
    in_ip_dict = self.get_in_ip_addr(tenant_id)
    in_gw = in_ip_dict.get('gateway')
    if in_gw is None:
        LOG.error('No FW service GW present')
        return False
    ret = self.os_helper.program_rtr_nwk_next_hop(router_id, in_gw, cidr)
    if not ret:
        LOG.error('Unable to program default router next hop %s', router_id)
        return False
    return True