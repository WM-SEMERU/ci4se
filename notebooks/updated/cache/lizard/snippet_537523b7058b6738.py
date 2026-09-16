def launch_action_group(self, action_id):
    header = BASE_HEADERS.copy()
    header['Cookie'] = self.__cookie
    request = requests.get(BASE_URL + 'launchActionGroup?oid=' + action_id,
        headers=header, timeout=10)
    if request.status_code != 200:
        self.__logged_in = False
        self.login()
        self.launch_action_group(action_id)
        return
    try:
        result = request.json()
    except ValueError as error:
        raise Exception('Not a valid result for launch' +
            'action group, protocol error: ' + request.status_code + ' - ' +
            request.reason + ' (' + error + ')')
    if 'actionGroup' not in result.keys():
        raise Exception('Could not launch action' + 'group, missing execId.')
    return result['actionGroup'][0]['execId']