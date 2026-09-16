def setSubgraphVal(self, parent_name, graph_name, field_name, val):
    subgraph = self._getSubGraph(parent_name, graph_name, True)
    if subgraph.hasField(field_name):
        subgraph.setVal(field_name, val)
    else:
        raise AttributeError(
            'Invalid field name %s for subgraph %s of parent graph %s.' % (
            field_name, graph_name, parent_name))