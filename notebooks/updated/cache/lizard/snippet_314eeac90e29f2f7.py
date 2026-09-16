def attach_intf_router(self, tenant_id, tenant_name, router_id):
    in_sub = self.get_in_subnet_id(tenant_id)
    out_sub = self.get_out_subnet_id(tenant_id)
    subnet_lst = set()
    subnet_lst.add(in_sub)
    subnet_lst.add(out_sub)
    ret = self.os_helper.add_intf_router(router_id, tenant_id, subnet_lst)
    return ret, in_sub, out_sub