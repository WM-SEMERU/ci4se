def solution_blobs(self, tx, tx_in_idx):
    sc = tx.SolutionChecker(tx)
    tx_context = sc.tx_context_for_idx(tx_in_idx)
    solution_stack = []
    for puzzle_script, solution_stack, flags, sighash_f in sc.puzzle_and_solution_iterator(
        tx_context):
        pass
    for s in solution_stack:
        yield s