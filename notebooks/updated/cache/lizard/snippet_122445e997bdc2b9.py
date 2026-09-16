def _helper(result, graph, number_edges_remaining: int, node_blacklist: Set
    [BaseEntity], invert_degrees: Optional[bool]=None):
    original_node_count = graph.number_of_nodes()
    log.debug('adding remaining %d edges', number_edges_remaining)
    for _ in range(number_edges_remaining):
        source, possible_step_nodes, c = None, set(), 0
        while not source or not possible_step_nodes:
            source = get_random_node(result, node_blacklist, invert_degrees
                =invert_degrees)
            c += 1
            if c >= original_node_count:
                log.warning('infinite loop happening')
                log.warning('source: %s', source)
                log.warning('no grow: %s', node_blacklist)
                return
            if source is None:
                continue
            possible_step_nodes = set(graph[source]) - set(result[source])
            if not possible_step_nodes:
                node_blacklist.add(source)
        step_node = random.choice(list(possible_step_nodes))
        key, attr_dict = random.choice(list(graph[source][step_node].items()))
        result.add_edge(source, step_node, key=key, **attr_dict)