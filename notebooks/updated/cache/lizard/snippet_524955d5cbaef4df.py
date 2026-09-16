def get_next_ip(self, tenant_id, direc):
    if direc == 'in':
        subnet_dict = self.get_in_ip_addr(tenant_id)
    else:
        subnet_dict = self.get_out_ip_addr(tenant_id)
    if subnet_dict:
        return subnet_dict
    if direc == 'in':
        ip_next = self.check_allocate_ip(self.service_in_ip, 'in')
    else:
        ip_next = self.check_allocate_ip(self.service_out_ip, 'out')
    return {'subnet': ip_next, 'start': self.get_start_ip(ip_next), 'end':
        self.get_end_ip(ip_next), 'gateway': self.get_gateway(ip_next),
        'sec_gateway': self.get_secondary_gateway(ip_next)}