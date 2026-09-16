def get_local_roles_for(brain_or_object, user=None):
    user_id = get_user_id(user)
    obj = api.get_object(brain_or_object)
    return sorted(obj.get_local_roles_for_userid(user_id))