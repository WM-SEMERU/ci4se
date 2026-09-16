def setup_name(self, name, address=None, transact={}):
    if not name:
        self._assert_control(address, 'the reverse record')
        return self._setup_reverse(None, address, transact=transact)
    else:
        resolved = self.address(name)
        if is_none_or_zero_address(address):
            address = resolved
        elif resolved and address != resolved and resolved != EMPTY_ADDR_HEX:
            raise AddressMismatch(
                'Could not set address %r to point to name, because the name resolves to %r. To change the name for an existing address, call setup_address() first.'
                 % (address, resolved))
        if is_none_or_zero_address(address):
            address = self.owner(name)
        if is_none_or_zero_address(address):
            raise UnownedName('claim subdomain using setup_address() first')
        if is_binary_address(address):
            address = to_checksum_address(address)
        if not is_checksum_address(address):
            raise ValueError('You must supply the address in checksum format')
        self._assert_control(address, name)
        if not resolved:
            self.setup_address(name, address, transact=transact)
        return self._setup_reverse(name, address, transact=transact)