def construct(start_block, vmap, exceptions):
    bfs_blocks = bfs(start_block)
    graph = Graph()
    gen_ret = GenInvokeRetName()
    block_to_node = {}
    exceptions_start_block = []
    for exception in exceptions:
        for _, _, block in exception.exceptions:
            exceptions_start_block.append(block)
    for block in bfs_blocks:
        node = make_node(graph, block, block_to_node, vmap, gen_ret)
        graph.add_node(node)
    graph.entry = block_to_node[start_block]
    del block_to_node, bfs_blocks
    graph.compute_rpo()
    graph.number_ins()
    for node in graph.rpo:
        preds = [pred for pred in graph.all_preds(node) if pred.num < node.num]
        if preds and all(pred.in_catch for pred in preds):
            node.in_catch = True
    lexit_nodes = [node for node in graph if node.type.is_return]
    if len(lexit_nodes) > 1:
        logger.error('Multiple exit nodes found !')
        graph.exit = graph.rpo[-1]
    elif len(lexit_nodes) < 1:
        logger.debug('No exit node found !')
    else:
        graph.exit = lexit_nodes[0]
    return graph