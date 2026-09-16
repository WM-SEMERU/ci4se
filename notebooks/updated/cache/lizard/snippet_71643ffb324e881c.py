def update_fw_local_router(self, net_id, subnet_id, router_id, os_result):
    fw_dict = self.get_fw_dict()
    fw_dict.update({'router_id': router_id, 'router_net_id': net_id,
        'router_subnet_id': subnet_id})
    self.store_dummy_router_net(net_id, subnet_id, router_id)
    self.update_fw_local_result(os_result=os_result)