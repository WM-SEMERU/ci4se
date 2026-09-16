def delete_os_dummy_rtr_nwk(self, rtr_id, net_id, subnet_id):
    subnet_lst = set()
    subnet_lst.add(subnet_id)
    ret = self.os_helper.delete_intf_router(None, None, rtr_id, subnet_lst)
    if not ret:
        return ret
    return self.os_helper.delete_network_all_subnets(net_id)