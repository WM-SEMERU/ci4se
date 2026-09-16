def _copy(self):
    table = {}
    for existingState, existingOutputs in self.table.items():
        table[existingState] = {}
        for existingInput, existingTransition in existingOutputs.items():
            table[existingState][existingInput] = existingTransition
    return TransitionTable(table)