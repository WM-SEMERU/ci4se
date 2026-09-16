def estimate_cpd(self, node):
    state_counts = self.state_counts(node)
    state_counts.ix[:, ((state_counts == 0).all())] = 1
    parents = sorted(self.model.get_parents(node))
    parents_cardinalities = [len(self.state_names[parent]) for parent in
        parents]
    node_cardinality = len(self.state_names[node])
    cpd = TabularCPD(node, node_cardinality, np.array(state_counts),
        evidence=parents, evidence_card=parents_cardinalities, state_names=
        self.state_names)
    cpd.normalize()
    return cpd