def inject_target(self, target, dependencies=None, derived_from=None,
    synthetic=False):
    if self.contains_address(target.address):
        raise ValueError(
            'Attempted to inject synthetic {target} derived from {derived_from} into the BuildGraph with address {address}, but there is already a Target {existing_target} with that address'
            .format(target=target, derived_from=derived_from, address=
            target.address, existing_target=self.get_target(target.address)))
    dependencies = dependencies or frozenset()
    address = target.address
    if address in self._target_by_address:
        raise ValueError(
            'A Target {existing_target} already exists in the BuildGraph at address {address}.  Failed to insert {target}.'
            .format(existing_target=self._target_by_address[address],
            address=address, target=target))
    if derived_from:
        if not self.contains_address(derived_from.address):
            raise ValueError(
                'Attempted to inject synthetic {target} derived from {derived_from} into the BuildGraph, but {derived_from} was not in the BuildGraph. Synthetic Targets must be derived from no Target (None) or from a Target already in the BuildGraph.'
                .format(target=target, derived_from=derived_from))
        self._derived_from_by_derivative[target.address] = derived_from.address
        self._derivatives_by_derived_from[derived_from.address].append(target
            .address)
    if derived_from or synthetic:
        self.synthetic_addresses.add(address)
    self._target_by_address[address] = target
    for dependency_address in dependencies:
        self.inject_dependency(dependent=address, dependency=dependency_address
            )