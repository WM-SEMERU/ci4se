def set_qinq_port(self, port_number, outer_vlan, ethertype):
    if port_number not in self._nios:
        raise DynamipsError('Port {} is not allocated'.format(port_number))
    nio = self._nios[port_number]
    if ethertype != '0x8100' and parse_version(self.hypervisor.version
        ) < parse_version('0.2.16'):
        raise DynamipsError(
            'Dynamips version required is >= 0.2.16 to change the default QinQ Ethernet type, detected version is {}'
            .format(self.hypervisor.version))
    yield from self._hypervisor.send(
        'ethsw set_qinq_port "{name}" {nio} {outer_vlan} {ethertype}'.
        format(name=self._name, nio=nio, outer_vlan=outer_vlan, ethertype=
        ethertype if ethertype != '0x8100' else ''))
    log.info(
        'Ethernet switch "{name}" [{id}]: port {port} set as a QinQ ({ethertype}) port with outer VLAN {vlan_id}'
        .format(name=self._name, id=self._id, port=port_number, vlan_id=
        outer_vlan, ethertype=ethertype))
    self._mappings[port_number] = 'qinq', outer_vlan, ethertype