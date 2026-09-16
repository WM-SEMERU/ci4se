def retry_failure_fab_dev_create(self, tenant_id, fw_data, fw_dict):
    result = fw_data.get('result').split('(')[0]
    is_fw_virt = self.is_device_virtual()
    if result == fw_constants.RESULT_FW_CREATE_INIT:
        name = dfa_dbm.DfaDBMixin.get_project_name(self, tenant_id)
        ret = self.fabric.retry_failure(tenant_id, name, fw_dict,
            is_fw_virt, result)
        if not ret:
            LOG.error('Retry failure returned fail for tenant %s', tenant_id)
            return
        else:
            result = fw_constants.RESULT_FW_CREATE_DONE
            self.update_fw_db_final_result(fw_dict.get('fw_id'), result)
    if result == fw_constants.RESULT_FW_CREATE_DONE:
        if fw_data.get('device_status') != 'SUCCESS':
            ret = self.create_fw_device(tenant_id, fw_dict.get('fw_id'),
                fw_dict)
            if ret:
                self.fwid_attr[tenant_id].fw_drvr_created(True)
                self.update_fw_db_dev_status(fw_dict.get('fw_id'), 'SUCCESS')
                LOG.info('Retry failue return success for create tenant %s',
                    tenant_id)