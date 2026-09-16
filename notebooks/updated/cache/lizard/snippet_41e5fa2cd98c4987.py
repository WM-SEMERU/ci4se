def add_resourcegroup(group, network_id, **kwargs):
    group_i = ResourceGroup()
    group_i.name = group.name
    group_i.description = group.description
    group_i.status = group.status
    group_i.network_id = network_id
    db.DBSession.add(group_i)
    db.DBSession.flush()
    return group_i