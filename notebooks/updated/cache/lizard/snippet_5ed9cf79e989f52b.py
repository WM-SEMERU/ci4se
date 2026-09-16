def check_allocate_ip(self, obj, direc):
    subnet_lst = self.os_helper.get_all_subnets_cidr(no_mask=True)
    ip_next = obj.allocate_subnet(subnet_lst)
    if ip_next is None:
        LOG.error('Unable to allocate a subnet for direction %s', direc)
    return ip_next