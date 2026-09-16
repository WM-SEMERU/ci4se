def user_exists_p(login, connector):
    url = '/users/' + login + '/'
    _r = connector.get(url)
    return _r.status_code == Constants.PULP_GET_OK