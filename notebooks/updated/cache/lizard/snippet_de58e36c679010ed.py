def _delete_os_nwk(self, tenant_id, tenant_name, direc, is_fw_virt=False):
    serv_obj = self.get_service_obj(tenant_id)
    fw_dict = serv_obj.get_fw_dict()
    fw_id = fw_dict.get('fw_id')
    fw_data, fw_data_dict = self.get_fw(fw_id)
    if fw_data is None:
        LOG.error('Unable to get fw_data for tenant %s', tenant_name)
        return False
    if direc == 'in':
        net_id = fw_data.in_network_id
        seg, vlan = self.get_in_seg_vlan(tenant_id)
        subnet_dict = self.get_in_ip_addr(tenant_id)
    else:
        net_id = fw_data.out_network_id
        seg, vlan = self.get_out_seg_vlan(tenant_id)
        subnet_dict = self.get_out_ip_addr(tenant_id)
    sub = subnet_dict.get('subnet')
    try:
        ret = self.os_helper.delete_network_all_subnets(net_id)
        if not ret:
            LOG.error('Delete network for ID %(net)s direct %(dir)s failed',
                {'net': net_id, 'dir': direc})
            return False
    except Exception as exc:
        LOG.error(
            'Delete network for ID %(net)s direct %(dir)s failed Exc %(exc)s',
            {'net': net_id, 'dir': direc, 'exc': exc})
        return False
    if not is_fw_virt:
        self.service_vlans.release_segmentation_id(vlan)
    self.service_segs.release_segmentation_id(seg)
    self.release_subnet(sub, direc)
    self.delete_network_db(net_id)
    return True