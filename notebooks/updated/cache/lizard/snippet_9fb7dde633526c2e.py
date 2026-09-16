def add_leaf_node(self, tree_id, node_id, values, relative_hit_rate=None):
    spec_node = self.tree_parameters.nodes.add()
    spec_node.treeId = tree_id
    spec_node.nodeId = node_id
    spec_node.nodeBehavior = (_TreeEnsemble_pb2.TreeEnsembleParameters.
        TreeNode.TreeNodeBehavior.Value('LeafNode'))
    if not isinstance(values, _collections.Iterable):
        values = [values]
    if relative_hit_rate is not None:
        spec_node.relativeHitRate = relative_hit_rate
    if type(values) == dict:
        iter = values.items()
    else:
        iter = enumerate(values)
    for index, value in iter:
        ev_info = spec_node.evaluationInfo.add()
        ev_info.evaluationIndex = index
        ev_info.evaluationValue = float(value)
        spec_node.nodeBehavior = (_TreeEnsemble_pb2.TreeEnsembleParameters.
            TreeNode.TreeNodeBehavior.Value('LeafNode'))