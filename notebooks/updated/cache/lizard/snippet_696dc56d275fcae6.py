def add_project(project, **kwargs):
    user_id = kwargs.get('user_id')
    existing_proj = get_project_by_name(project.name, user_id=user_id)
    if len(existing_proj) > 0:
        raise HydraError('A Project with the name "%s" already exists' % (
            project.name,))
    proj_i = Project()
    proj_i.name = project.name
    proj_i.description = project.description
    proj_i.created_by = user_id
    attr_map = hdb.add_resource_attributes(proj_i, project.attributes)
    db.DBSession.flush()
    proj_data = _add_project_attribute_data(proj_i, attr_map, project.
        attribute_data)
    proj_i.attribute_data = proj_data
    proj_i.set_owner(user_id)
    db.DBSession.add(proj_i)
    db.DBSession.flush()
    return proj_i