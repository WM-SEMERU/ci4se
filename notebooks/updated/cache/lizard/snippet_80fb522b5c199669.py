def _create_arg_dict(self, tenant_id, data, in_sub, out_sub):
    in_seg, in_vlan = self.get_in_seg_vlan(tenant_id)
    out_seg, out_vlan = self.get_out_seg_vlan(tenant_id)
    in_ip_dict = self.get_in_ip_addr(tenant_id)
    out_ip_dict = self.get_out_ip_addr(tenant_id)
    excl_list = [in_ip_dict.get('subnet'), out_ip_dict.get('subnet')]
    arg_dict = {'tenant_id': tenant_id, 'tenant_name': data.get(
        'tenant_name'), 'in_seg': in_seg, 'in_vlan': in_vlan, 'out_seg':
        out_seg, 'out_vlan': out_vlan, 'router_id': data.get('router_id'),
        'in_sub': in_sub, 'out_sub': out_sub, 'in_gw': in_ip_dict.get(
        'gateway'), 'out_gw': out_ip_dict.get('gateway'), 'excl_list':
        excl_list}
    return arg_dict