def delete_usage_plan(plan_id, region=None, key=None, keyid=None, profile=None
    ):
    try:
        existing = describe_usage_plans(plan_id=plan_id, region=region, key
            =key, keyid=keyid, profile=profile)
        if 'error' in existing:
            return {'error': existing['error']}
        if 'plans' in existing and existing['plans']:
            conn = _get_conn(region=region, key=key, keyid=keyid, profile=
                profile)
            res = conn.delete_usage_plan(usagePlanId=plan_id)
        return {'deleted': True, 'usagePlanId': plan_id}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}