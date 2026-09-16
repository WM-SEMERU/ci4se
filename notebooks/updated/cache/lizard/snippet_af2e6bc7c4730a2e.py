def get_max_instances_of_storage_bus(self, chipset, bus):
    if not isinstance(chipset, ChipsetType):
        raise TypeError('chipset can only be an instance of type ChipsetType')
    if not isinstance(bus, StorageBus):
        raise TypeError('bus can only be an instance of type StorageBus')
    max_instances = self._call('getMaxInstancesOfStorageBus', in_p=[chipset,
        bus])
    return max_instances