def wait_for_contract(self, contract_address_hex, timeout=None):
    contract_address = decode_hex(contract_address_hex)
    start_time = time.time()
    result = self._raiden.chain.client.web3.eth.getCode(to_checksum_address
        (contract_address))
    current_time = time.time()
    while not result:
        if timeout and start_time + timeout > current_time:
            return False
        result = self._raiden.chain.client.web3.eth.getCode(to_checksum_address
            (contract_address))
        gevent.sleep(0.5)
        current_time = time.time()
    return len(result) > 0