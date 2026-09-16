def get_elimination_order(self, nodes=None):
    if not nodes:
        nodes = self.bayesian_model.nodes()
    nodes = set(nodes)
    ordering = []
    while nodes:
        scores = {node: self.cost(node) for node in nodes}
        min_score_node = min(scores, key=scores.get)
        ordering.append(min_score_node)
        nodes.remove(min_score_node)
    return ordering