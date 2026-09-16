def get_groups(network_id, template_id=None, **kwargs):
    user_id = kwargs.get('user_id')
    try:
        net_i = db.DBSession.query(Network).filter(Network.id == network_id
            ).one()
        net_i.check_read_permission(user_id=user_id)
    except NoResultFound:
        raise ResourceNotFoundError('Network %s not found' % network_id)
    group_qry = db.DBSession.query(ResourceGroup).filter(ResourceGroup.
        network_id == network_id, ResourceGroup.status == 'A').options(noload
        ('network')).options(joinedload_all('types.templatetype')).options(
        joinedload_all('attributes.attr'))
    if template_id is not None:
        group_qry = group_qry.filter(ResourceType.group_id == ResourceGroup
            .id, TemplateType.id == ResourceType.type_id, TemplateType.
            template_id == template_id)
    groups = group_qry.all()
    return groups