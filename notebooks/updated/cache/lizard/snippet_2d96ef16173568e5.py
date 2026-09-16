def get_subnets():
    LOGGER.debug('SubnetService.get_subnets')
    args = {'http_operation': 'GET', 'operation_path': ''}
    response = SubnetService.requester.call(args)
    ret = None
    if response.rc == 0:
        ret = []
        for subnet in response.response_content['subnets']:
            ret.append(Subnet.json_2_subnet(subnet))
    elif response.rc != 404:
        err_msg = (
            'SubnetService.get_subnets - Problem while getting subnets. . Reason: '
             + str(response.response_content) + '-' + str(response.
            error_message) + ' (' + str(response.rc) + ')')
        LOGGER.warning(err_msg)
    return ret