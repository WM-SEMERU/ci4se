def node_received_infos(node_id):
    exp = Experiment(session)
    info_type = request_parameter(parameter='info_type', parameter_type=
        'known_class', default=models.Info)
    if type(info_type) == Response:
        return info_type
    node = models.Node.query.get(node_id)
    if node is None:
        return error_response(error_type=
            '/node/infos, node {} does not exist'.format(node_id))
    infos = node.received_infos(type=info_type)
    try:
        exp.info_get_request(node=node, infos=infos)
        session.commit()
    except Exception:
        return error_response(error_type='info_get_request error', status=
            403, participant=node.participant)
    return success_response(infos=[i.__json__() for i in infos])