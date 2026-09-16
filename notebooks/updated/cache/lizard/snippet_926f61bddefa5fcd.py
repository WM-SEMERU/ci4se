def _get_host_details(self):
    status, headers, system = self._rest_get('/rest/v1/Systems/1')
    if status < 300:
        stype = self._get_type(system)
        if stype not in ['ComputerSystem.0', 'ComputerSystem.1']:
            msg = '%s is not a valid system type ' % stype
            raise exception.IloError(msg)
    else:
        msg = self._get_extended_error(system)
        raise exception.IloError(msg)
    return system