def _create_intermediate_target(self, address, suffix):
    if not isinstance(address, string_types):
        raise self.ExpectedAddressError(
            'Expected string address argument, got type {type}'.format(type
            =type(address)))
    address = Address.parse(address, self._parse_context.rel_path)
    hash_str = hash_target(str(address), suffix)
    name = '{name}-unstable-{suffix}-{index}'.format(name=address.
        target_name, suffix=suffix.replace(' ', '.'), index=hash_str)
    self._parse_context.create_object_if_not_exists('target', name=name,
        dependencies=[address.spec], **self.extra_target_arguments)
    return ':{}'.format(name)