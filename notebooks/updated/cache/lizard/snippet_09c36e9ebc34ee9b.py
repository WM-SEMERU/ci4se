def get_teams():
    LOGGER.debug('TeamService.get_teams')
    args = {'http_operation': 'GET', 'operation_path': ''}
    response = TeamService.requester.call(args)
    ret = None
    if response.rc == 0:
        ret = []
        for team in response.response_content['teams']:
            ret.append(Team.json_2_team(team))
    elif response.rc != 404:
        err_msg = (
            'TeamService.get_teams - Problem while getting teams. . Reason: ' +
            str(response.response_content) + '-' + str(response.
            error_message) + ' (' + str(response.rc) + ')')
        LOGGER.warning(err_msg)
    return ret