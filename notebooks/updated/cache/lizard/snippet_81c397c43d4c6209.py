def delete_nic(self, instance_id, port_id):
    self.client.servers.interface_detach(instance_id, port_id)
    return True