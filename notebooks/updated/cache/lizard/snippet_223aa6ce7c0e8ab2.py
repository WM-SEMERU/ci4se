def create_os_dummy_rtr(self, tenant_id, fw_dict, is_fw_virt=False):
    res = fw_const.OS_DUMMY_RTR_CREATE_SUCCESS
    tenant_name = fw_dict.get('tenant_name')
    try:
        rtr_id = fw_dict.get('router_id')
        if rtr_id is None:
            LOG.error('Invalid router id, attaching dummy interface failed')
            return False
        if is_fw_virt:
            net_id = subnet_id = None
        else:
            net_id, subnet_id = self._attach_dummy_intf_rtr(tenant_id,
                tenant_name, rtr_id)
            if net_id is None or subnet_id is None:
                LOG.error(
                    'Invalid net_id or subnet_id, creating dummy interface failed'
                    )
                return False
    except Exception as exc:
        LOG.error(
            'Creation of Openstack Router failed tenant %(tenant)s, Exception %(exc)s'
            , {'tenant': tenant_id, 'exc': str(exc)})
        res = fw_const.OS_DUMMY_RTR_CREATE_FAIL
    self.store_fw_db_router(tenant_id, net_id, subnet_id, rtr_id, res)
    return True