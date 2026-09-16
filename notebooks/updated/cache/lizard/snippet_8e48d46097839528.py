def _get_id_from_username(self, username):
    _mask = 'mask[id, username]'
    _filter = {'users': {'username': utils.query_filter(username)}}
    user = self.list_users(_mask, _filter)
    if len(user) == 1:
        return [user[0]['id']]
    elif len(user) > 1:
        raise exceptions.SoftLayerError(
            'Multiple users found with the name: %s' % username)
    else:
        raise exceptions.SoftLayerError('Unable to find user id for %s' %
            username)