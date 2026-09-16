def restart_policy(val, **kwargs):
    val = helpers.map_vals(val, 'Name', 'MaximumRetryCount', fill='0')
    if len(val) != 1:
        raise SaltInvocationError('Only one policy is permitted')
    val = val[0]
    try:
        val['MaximumRetryCount'] = int(val['MaximumRetryCount'])
    except (TypeError, ValueError):
        raise SaltInvocationError("Retry count '{0}' is non-numeric".format
            (val['MaximumRetryCount']))
    return val