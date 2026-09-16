def adapter_update_nio_binding(self, adapter_number, nio):
    if self.is_running():
        try:
            yield from self.update_ubridge_udp_connection('VBOX-{}-{}'.
                format(self._id, adapter_number), self._local_udp_tunnels[
                adapter_number][1], nio)
        except IndexError:
            raise VirtualBoxError(
                'Adapter {adapter_number} does not exist on VirtualBox VM "{name}"'
                .format(name=self._name, adapter_number=adapter_number))