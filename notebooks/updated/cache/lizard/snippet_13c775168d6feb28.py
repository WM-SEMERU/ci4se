def whitelist(self, address: Address):
    self.log.debug('Whitelist', address=to_normalized_address(address))
    self._address_mgr.add_address(address)