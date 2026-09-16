def get_statements(self, filter=False):
    bp_stmts = self.get_biopax_stmts(filter=filter)
    bel_stmts = self.get_bel_stmts(filter=filter)
    return bp_stmts + bel_stmts