def update_fw_db_result(self, tenant_id, os_status=None, dcnm_status=None,
    dev_status=None):
    serv_obj = self.get_service_obj(tenant_id)
    serv_obj.update_fw_local_result(os_status, dcnm_status, dev_status)
    serv_obj.commit_fw_db_result()