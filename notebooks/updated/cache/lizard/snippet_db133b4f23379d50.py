def deliver_tx(self, raw_transaction):
    self.abort_if_abci_chain_is_not_synced()
    logger.debug('deliver_tx: %s', raw_transaction)
    transaction = self.bigchaindb.is_valid_transaction(decode_transaction(
        raw_transaction), self.block_transactions)
    if not transaction:
        logger.debug('deliver_tx: INVALID')
        return ResponseDeliverTx(code=CodeTypeError)
    else:
        logger.debug('storing tx')
        self.block_txn_ids.append(transaction.id)
        self.block_transactions.append(transaction)
        return ResponseDeliverTx(code=CodeTypeOk)