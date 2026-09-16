def set_domain(clz, dag):
    logging.info('Setting domain for poset %s' % clz.__name__)
    if nx.number_of_nodes(dag) == 0:
        raise CellConstructionFailure('Empty DAG structure.')
    if not nx.is_directed_acyclic_graph(dag):
        raise CellConstructionFailure('Must be directed and acyclic')
    if not nx.is_weakly_connected(dag):
        raise CellConstructionFailure('Must be connected')
    clz.domain_map[clz] = dag