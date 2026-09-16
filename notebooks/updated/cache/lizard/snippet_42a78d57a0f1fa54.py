def delete_fabric_fw_internal(self, tenant_id, fw_dict, is_fw_virt, result):
    if not self.auto_nwk_create:
        LOG.info('Auto network creation disabled')
        return False
    try:
        tenant_name = fw_dict.get('tenant_name')
        fw_name = fw_dict.get('fw_name')
        if tenant_id not in self.service_attr:
            LOG.error('Service obj not created for tenant %s', tenant_name)
            return False
        if result == fw_const.RESULT_FW_DELETE_DONE:
            LOG.error('Fabric for tenant %s already deleted', tenant_id)
            return True
        ret = self.run_delete_sm(tenant_id, fw_dict, is_fw_virt)
        self.service_attr[tenant_id].set_fabric_create(False)
        if ret:
            LOG.info(
                'Delete SM completed successfully for tenant%(tenant)s FW %(fw)s'
                , {'tenant': tenant_name, 'fw': fw_name})
            self.service_attr[tenant_id].destroy_local_fw_db()
            self.delete_serv_obj(tenant_id)
        else:
            LOG.error('Delete SM failed for tenant%(tenant)s FW %(fw)s', {
                'tenant': tenant_name, 'fw': fw_name})
    except Exception as exc:
        LOG.error('Exception raised in delete fabric int %s', str(exc))
        return False
    return ret