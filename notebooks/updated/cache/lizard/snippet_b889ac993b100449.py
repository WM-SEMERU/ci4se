def put_targets(Rule, Targets, region=None, key=None, keyid=None, profile=None
    ):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if isinstance(Targets, six.string_types):
            Targets = salt.utils.json.loads(Targets)
        failures = conn.put_targets(Rule=Rule, Targets=Targets)
        if failures and failures.get('FailedEntryCount', 0) > 0:
            return {'failures': failures.get('FailedEntries')}
        else:
            return {'failures': None}
    except ClientError as e:
        err = __utils__['boto3.get_error'](e)
        if e.response.get('Error', {}).get('Code') == 'RuleNotFoundException':
            return {'error': 'Rule {0} not found'.format(Rule)}
        return {'error': __utils__['boto3.get_error'](e)}