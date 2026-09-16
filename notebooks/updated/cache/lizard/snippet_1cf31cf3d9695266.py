def causally_significant_nodes(cm):
    inputs = cm.sum(0)
    outputs = cm.sum(1)
    nodes_with_inputs_and_outputs = np.logical_and(inputs > 0, outputs > 0)
    return tuple(np.where(nodes_with_inputs_and_outputs)[0])