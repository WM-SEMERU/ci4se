def find_subnet(sb_id=None, sb_name=None):
    LOGGER.debug('SubnetService.find_subnet')
    if (sb_id is None or not sb_id) and (sb_name is None or not sb_name):
        raise exceptions.ArianeCallParametersError('id and name')
    if (sb_id is not None and sb_id) and (sb_name is not None and sb_name):
        LOGGER.warn('Both id and name are defined. Will give you search on id.'
            )
        sb_name = None
    params = None
    if sb_id is not None and sb_id:
        params = {'id': sb_id}
    elif sb_name is not None and sb_name:
        params = {'name': sb_name}
    ret = None
    if params is not None:
        args = {'http_operation': 'GET', 'operation_path': 'get',
            'parameters': params}
        response = SubnetService.requester.call(args)
        if response.rc == 0:
            ret = Subnet.json_2_subnet(response.response_content)
        elif response.rc != 404:
            err_msg = (
                'SubnetService.find_subnet - Problem while finding subnet (id:'
                 + str(sb_id) + ', name:' + str(sb_name) + '). ' +
                '. Reason: ' + str(response.response_content) + '-' + str(
                response.error_message) + ' (' + str(response.rc) + ')')
            LOGGER.warning(err_msg)
    return ret