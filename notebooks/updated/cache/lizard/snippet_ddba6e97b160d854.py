def connect(self, chassis_list):
    self._check_session()
    if not isinstance(chassis_list, (list, tuple, set, dict, frozenset)):
        chassis_list = chassis_list,
    if len(chassis_list) == 1:
        status, data = self._rest.put_request('connections', chassis_list[0])
        data = [data]
    else:
        params = {chassis: True for chassis in chassis_list}
        params['action'] = 'connect'
        status, data = self._rest.post_request('connections', None, params)
    return data