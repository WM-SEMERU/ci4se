def mock(self, slot, rpc_id, value):
    address = slot.address
    if address not in self.mock_rpcs:
        self.mock_rpcs[address] = {}
    self.mock_rpcs[address][rpc_id] = value