def is_contextfree(self):
    for lhs, rhs in self.rules:
        if len(lhs) != 1:
            return False
        if lhs[0] not in self.nonterminals:
            return False
    return True