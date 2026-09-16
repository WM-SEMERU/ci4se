def schedule_downtime(scope, api_key=None, app_key=None, monitor_id=None,
    start=None, end=None, message=None, recurrence=None, timezone=None,
    test=False):
    ret = {'result': False, 'response': None, 'comment': ''}
    if api_key is None:
        raise SaltInvocationError('api_key must be specified')
    if app_key is None:
        raise SaltInvocationError('app_key must be specified')
    if test is True:
        ret['result'] = True
        ret['comment'] = 'A schedule downtime API call would have been made.'
        return ret
    _initialize_connection(api_key, app_key)
    try:
        response = datadog.api.Downtime.create(scope=scope, monitor_id=
            monitor_id, start=start, end=end, message=message, recurrence=
            recurrence, timezone=timezone)
    except ValueError:
        comment = (
            'Unexpected exception in Datadog Schedule Downtime API call. Are your keys correct?'
            )
        ret['comment'] = comment
        return ret
    ret['response'] = response
    if 'active' in response.keys():
        ret['result'] = True
        ret['comment'] = 'Successfully scheduled downtime'
    return ret