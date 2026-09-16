def append_formula(self, formula, no_return=True):
    if self.lingeling:
        for clause in formula:
            self.add_clause(clause, no_return)