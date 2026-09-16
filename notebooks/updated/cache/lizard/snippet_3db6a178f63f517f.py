def create_replication_interface(self, sp, ip_port, ip_address, netmask=
    None, v6_prefix_length=None, gateway=None, vlan_id=None):
    return UnityReplicationInterface.create(self._cli, sp, ip_port,
        ip_address, netmask=netmask, v6_prefix_length=v6_prefix_length,
        gateway=gateway, vlan_id=vlan_id)