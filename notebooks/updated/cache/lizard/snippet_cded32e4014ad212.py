def lock(thing_name, lock, key, session=None):
    return _request('get', '/lock/{0}'.format(thing_name), params={'key':
        key, 'lock': lock}, session=session)