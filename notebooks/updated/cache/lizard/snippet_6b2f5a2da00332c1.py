def _process(self, startblock):
    log.debug('Processing blocks %d to %d' % (startblock, startblock +
        BATCH_SIZE))
    addresses = []
    for blockNum in range(startblock, startblock + BATCH_SIZE):
        block_hash = self.db.reader._get_block_hash(blockNum)
        if block_hash is not None:
            receipts = self.db.reader._get_block_receipts(block_hash, blockNum)
            for receipt in receipts:
                if receipt.contractAddress is not None and not all(b == 0 for
                    b in receipt.contractAddress):
                    addresses.append(receipt.contractAddress)
        elif len(addresses) == 0:
            raise Exception()
    return addresses