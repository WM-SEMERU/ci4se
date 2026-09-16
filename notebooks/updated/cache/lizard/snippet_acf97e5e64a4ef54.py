def discardTxns(self, count: int):
    if count == 0:
        return
    if count > len(self.uncommittedTxns):
        raise LogicError('expected to revert {} txns while there are only {}'
            .format(count, len(self.uncommittedTxns)))
    old_hash = self.uncommittedRootHash
    self.uncommittedTxns = self.uncommittedTxns[:-count]
    if not self.uncommittedTxns:
        self.uncommittedTree = None
        self.uncommittedRootHash = None
    else:
        self.uncommittedTree = self.treeWithAppliedTxns(self.uncommittedTxns)
        self.uncommittedRootHash = self.uncommittedTree.root_hash
    logger.info(
        'Discarding {} txns and root hash {} and new root hash is {}. {} are still uncommitted'
        .format(count, Ledger.hashToStr(old_hash), Ledger.hashToStr(self.
        uncommittedRootHash), len(self.uncommittedTxns)))