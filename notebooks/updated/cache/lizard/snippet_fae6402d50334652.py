def vlan_pvlan_association_add(self, **kwargs):
    name = kwargs.pop('name')
    sec_vlan = kwargs.pop('sec_vlan')
    callback = kwargs.pop('callback', self._callback)
    if not pynos.utilities.valid_vlan_id(name):
        raise InvalidVlanId('Incorrect name value.')
    if not pynos.utilities.valid_vlan_id(sec_vlan):
        raise InvalidVlanId('`sec_vlan` must be between `1` and `8191`.')
    pvlan_args = dict(name=name, sec_assoc_add=sec_vlan)
    pvlan_assoc = getattr(self._interface,
        'interface_vlan_interface_vlan_private_vlan_association_sec_assoc_add')
    config = pvlan_assoc(**pvlan_args)
    return callback(config)