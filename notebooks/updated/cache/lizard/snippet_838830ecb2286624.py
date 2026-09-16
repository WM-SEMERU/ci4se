def add_nodes(network_id, nodes, **kwargs):
    start_time = datetime.datetime.now()
    names = []
    for n_i in nodes:
        if n_i.name in names:
            raise HydraError('Duplicate Node Name: %s' % n_i.name)
        names.append(n_i.name)
    user_id = kwargs.get('user_id')
    try:
        net_i = db.DBSession.query(Network).filter(Network.id == network_id
            ).one()
        net_i.check_write_permission(user_id)
    except NoResultFound:
        raise ResourceNotFoundError('Network %s not found' % network_id)
    _add_nodes_to_database(net_i, nodes)
    net_i.project_id = net_i.project_id
    db.DBSession.flush()
    node_s = db.DBSession.query(Node).filter(Node.network_id == network_id
        ).all()
    node_id_map = dict()
    iface_nodes = dict()
    for n_i in node_s:
        iface_nodes[n_i.name] = n_i
    for node in nodes:
        node_id_map[node.id] = iface_nodes[node.name]
    _bulk_add_resource_attrs(network_id, 'NODE', nodes, iface_nodes)
    log.info('Nodes added in %s', get_timing(start_time))
    return node_s