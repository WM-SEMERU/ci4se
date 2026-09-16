def getLogs(self, argument_filters=None, fromBlock=None, toBlock=None,
    blockHash=None):
    if not self.address:
        raise TypeError(
            'This method can be only called on an instated contract with an address'
            )
    abi = self._get_event_abi()
    if argument_filters is None:
        argument_filters = dict()
    _filters = dict(**argument_filters)
    blkhash_set = blockHash is not None
    blknum_set = fromBlock is not None or toBlock is not None
    if blkhash_set and blknum_set:
        raise ValidationError(
            'blockHash cannot be set at the same time as fromBlock or toBlock')
    data_filter_set, event_filter_params = construct_event_filter_params(abi,
        contract_address=self.address, argument_filters=_filters, fromBlock
        =fromBlock, toBlock=toBlock, address=self.address)
    if blockHash is not None:
        event_filter_params['blockHash'] = blockHash
    logs = self.web3.eth.getLogs(event_filter_params)
    return tuple(get_event_data(abi, entry) for entry in logs)