def unshare_project(project_id, usernames, **kwargs):
    user_id = kwargs.get('user_id')
    proj_i = _get_project(project_id)
    proj_i.check_share_permission(user_id)
    for username in usernames:
        user_i = _get_user(username)
        proj_i.unset_owner(user_i.id, write=write, share=share)
    db.DBSession.flush()