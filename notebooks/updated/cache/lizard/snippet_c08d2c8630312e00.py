def delete_port_binding(self, port, host):
    if not self.get_instance_type(port):
        return
    for pb_key in self._get_binding_keys(port, host):
        pb_res = MechResource(pb_key, a_const.PORT_BINDING_RESOURCE,
            a_const.DELETE)
        self.provision_queue.put(pb_res)