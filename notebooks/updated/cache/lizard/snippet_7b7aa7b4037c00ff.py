def get_transports():
    LOGGER.debug('TransportService.get_transports')
    params = SessionService.complete_transactional_req(None)
    if params is None:
        if MappingService.driver_type != DriverFactory.DRIVER_REST:
            params = {'OPERATION': 'getTransports'}
            args = {'properties': params}
        else:
            args = {'http_operation': 'GET', 'operation_path': ''}
    elif MappingService.driver_type != DriverFactory.DRIVER_REST:
        params['OPERATION'] = 'getTransports'
        args = {'properties': params}
    else:
        args = {'http_operation': 'GET', 'operation_path': '', 'parameters':
            params}
    response = TransportService.requester.call(args)
    if MappingService.driver_type != DriverFactory.DRIVER_REST:
        response = response.get()
    ret = None
    if response.rc == 0:
        ret = []
        for transport in response.response_content['transports']:
            ret.append(Transport.json_2_transport(transport))
    elif response.rc != 404:
        err_msg = (
            'TransportService.get_transports - Problem while getting transports. Reason: '
             + str(response.response_content) + ' - ' + str(response.
            error_message) + ' (' + str(response.rc) + ')')
        LOGGER.warning(err_msg)
        if (response.rc == 500 and ArianeMappingOverloadError.ERROR_MSG in
            response.error_message):
            raise ArianeMappingOverloadError('Transport.get_transports',
                ArianeMappingOverloadError.ERROR_MSG)
    return ret