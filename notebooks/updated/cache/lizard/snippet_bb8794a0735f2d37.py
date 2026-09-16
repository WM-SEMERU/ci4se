def get_routing_areas():
    LOGGER.debug('RoutingAreaService.get_routing_areas')
    args = {'http_operation': 'GET', 'operation_path': ''}
    response = RoutingAreaService.requester.call(args)
    ret = None
    if response.rc == 0:
        ret = []
        for routing_area in response.response_content['routingAreas']:
            ret.append(RoutingArea.json_2_routing_area(routing_area))
    elif response.rc != 404:
        err_msg = (
            'RoutingAreaService.get_routing_areas - Problem while getting routing areas. Reason: '
             + str(response.response_content) + '-' + str(response.
            error_message) + ' (' + str(response.rc) + ')')
        LOGGER.warning(err_msg)
    return ret