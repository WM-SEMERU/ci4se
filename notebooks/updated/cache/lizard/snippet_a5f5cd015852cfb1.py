def remove_user_from_group(group, role, email):
    uri = 'groups/{0}/{1}/{2}'.format(group, role, email)
    return __delete(uri)