def _assemble_gap(self, stmt):
    gap = deepcopy(stmt.gap)
    gap.activity = ActivityCondition('gap', True)
    ras = deepcopy(stmt.ras)
    ras.activity = ActivityCondition('gtpbound', True)
    self._add_nodes_edges(gap, ras, pc.DIRECTLY_DECREASES, stmt.evidence)