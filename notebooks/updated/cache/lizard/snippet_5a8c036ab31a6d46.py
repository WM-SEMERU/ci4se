def _find_relevant_nodes(query_nodes, relevance_network, relevance_node_lim):
    all_nodes = relevance_client.get_relevant_nodes(relevance_network,
        query_nodes)
    nodes = [n[0] for n in all_nodes[:relevance_node_lim]]
    return nodes