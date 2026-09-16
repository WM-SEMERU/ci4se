def node_neighbors(node_id):
    exp = Experiment(session)
    node_type = request_parameter(parameter='node_type', parameter_type=
        'known_class', default=models.Node)
    connection = request_parameter(parameter='connection', default='to')
    failed = request_parameter(parameter='failed', parameter_type='bool',
        optional=True)
    for x in [node_type, connection]:
        if type(x) == Response:
            return x
    node = models.Node.query.get(node_id)
    if node is None:
        return error_response(error_type=
            '/node/neighbors, node does not exist', error_text=
            '/node/{0}/neighbors, node {0} does not exist'.format(node_id))
    if failed is not None:
        try:
            node.neighbors(type=node_type, direction=connection, failed=failed)
        except Exception as e:
            return error_response(error_type='node.neighbors', error_text=
                str(e))
    else:
        nodes = node.neighbors(type=node_type, direction=connection)
        try:
            exp.node_get_request(node=node, nodes=nodes)
            session.commit()
        except Exception:
            return error_response(error_type='exp.node_get_request')
    return success_response(nodes=[n.__json__() for n in nodes])