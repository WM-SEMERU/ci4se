def get_network_by_name(project_id, network_name, **kwargs):
    try:
        res = db.DBSession.query(Network.id).filter(func.lower(Network.name
            ).like(network_name.lower()), Network.project_id == project_id
            ).one()
        net = get_network(res.id, 'Y', None, **kwargs)
        return net
    except NoResultFound:
        raise ResourceNotFoundError('Network with name %s not found' %
            network_name)