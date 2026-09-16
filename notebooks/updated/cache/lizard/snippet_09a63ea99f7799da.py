def dependencies_of(self, address):
    assert address in self._target_by_address, 'Cannot retrieve dependencies of {address} because it is not in the BuildGraph.'.format(
        address=address)
    return self._target_dependencies_by_address[address]