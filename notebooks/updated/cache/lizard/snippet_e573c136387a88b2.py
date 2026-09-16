def ansible_inventory(self, keys=['vm-type', 'groups', 'vm-provider']):
    lansible = LagoAnsible(self._prefix)
    return lansible.get_inventory_str(keys=keys)