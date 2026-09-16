def set_qos(self, port_name, type='linux-htb', max_rate=None, queues=None):
    queues = queues if queues else []
    command_qos = ovs_vsctl.VSCtlCommand('set-qos', [port_name, type, max_rate]
        )
    command_queue = ovs_vsctl.VSCtlCommand('set-queue', [port_name, queues])
    self.run_command([command_qos, command_queue])
    if command_qos.result and command_queue.result:
        return command_qos.result + command_queue.result
    return None