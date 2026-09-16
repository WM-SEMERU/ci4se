def tx_context_for_idx(self, tx_in_idx):
    tx_in = self.tx.txs_in[tx_in_idx]
    tx_context = TxContext()
    tx_context.lock_time = self.tx.lock_time
    tx_context.version = self.tx.version
    tx_context.puzzle_script = b'' if self.tx.missing_unspent(tx_in_idx
        ) else self.tx.unspents[tx_in_idx].script
    tx_context.solution_script = tx_in.script
    tx_context.witness_solution_stack = tx_in.witness
    tx_context.sequence = tx_in.sequence
    tx_context.tx_in_idx = tx_in_idx
    return tx_context