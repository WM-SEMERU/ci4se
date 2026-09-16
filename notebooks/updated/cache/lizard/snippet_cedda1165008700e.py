def clear_dcnm_in_part(self, tenant_id, fw_dict, is_fw_virt=False):
    res = fw_const.DCNM_IN_PART_UPDDEL_SUCCESS
    tenant_name = fw_dict.get('tenant_name')
    ret = True
    try:
        self._update_partition_in_delete(tenant_name)
    except Exception as exc:
        LOG.error(
            'Clear of In Partition failed for tenant %(tenant)s , Exception %(exc)s'
            , {'tenant': tenant_id, 'exc': str(exc)})
        res = fw_const.DCNM_IN_PART_UPDDEL_FAIL
        ret = False
    self.update_fw_db_result(tenant_id, dcnm_status=res)
    LOG.info('In partition cleared off service ip addr')
    return ret