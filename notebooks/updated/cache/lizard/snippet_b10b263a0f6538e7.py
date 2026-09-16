def _index_target(self, target_adaptor):
    address = target_adaptor.address
    target = self._instantiate_target(target_adaptor)
    self._target_by_address[address] = target
    for dependency in target_adaptor.dependencies:
        if dependency in self._target_dependencies_by_address[address]:
            raise self.DuplicateAddressError(
                "Addresses in dependencies must be unique. '{spec}' is referenced more than once by target '{target}'."
                .format(spec=dependency.spec, target=address.spec))
        self._target_dependencies_by_address[address].add(dependency)
        self._target_dependees_by_address[dependency].add(address)
    return target