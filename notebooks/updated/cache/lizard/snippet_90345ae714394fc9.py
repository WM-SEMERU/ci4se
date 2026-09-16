def delete_project(project_id, **kwargs):
    user_id = kwargs.get('user_id')
    project = _get_project(project_id)
    project.check_write_permission(user_id)
    db.DBSession.delete(project)
    db.DBSession.flush()
    return 'OK'