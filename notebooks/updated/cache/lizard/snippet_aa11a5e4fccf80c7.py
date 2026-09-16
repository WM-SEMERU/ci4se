def post_data(api_key=None, name='OpsGenie Execution Module', reason=None,
    action_type=None):
    if api_key is None or reason is None:
        raise salt.exceptions.SaltInvocationError(
            'API Key or Reason cannot be None.')
    data = dict()
    data['alias'] = name
    data['message'] = reason
    data['cpuModel'] = __grains__['cpu_model']
    data['cpuArch'] = __grains__['cpuarch']
    data['fqdn'] = __grains__['fqdn']
    data['host'] = __grains__['host']
    data['id'] = __grains__['id']
    data['kernel'] = __grains__['kernel']
    data['kernelRelease'] = __grains__['kernelrelease']
    data['master'] = __grains__['master']
    data['os'] = __grains__['os']
    data['saltPath'] = __grains__['saltpath']
    data['saltVersion'] = __grains__['saltversion']
    data['username'] = __grains__['username']
    data['uuid'] = __grains__['uuid']
    log.debug('Below data will be posted:\n%s', data)
    log.debug('API Key: %s \t API Endpoint: %s', api_key, API_ENDPOINT)
    if action_type == 'Create':
        response = requests.post(url=API_ENDPOINT, data=salt.utils.json.
            dumps(data), headers={'Content-Type': 'application/json',
            'Authorization': 'GenieKey ' + api_key})
    else:
        response = requests.post(url=API_ENDPOINT + '/' + name +
            '/close?identifierType=alias', data=salt.utils.json.dumps(data),
            headers={'Content-Type': 'application/json', 'Authorization': 
            'GenieKey ' + api_key})
    return response.status_code, response.text