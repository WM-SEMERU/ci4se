def create_dcnm_out_nwk(self, tenant_id, fw_dict, is_fw_virt=False):
    tenant_name = fw_dict.get('tenant_name')
    ret = self._create_service_nwk(tenant_id, tenant_name, 'out')
    if ret:
        res = fw_const.DCNM_OUT_NETWORK_CREATE_SUCCESS
        LOG.info('out Service network created for tenant %s', tenant_id)
    else:
        res = fw_const.DCNM_OUT_NETWORK_CREATE_FAIL
        LOG.info('out Service network create failed for tenant %s', tenant_id)
    self.update_fw_db_result(tenant_id, dcnm_status=res)
    return ret