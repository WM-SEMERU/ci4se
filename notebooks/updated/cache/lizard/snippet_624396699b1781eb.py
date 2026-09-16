def create(name, template_body=None, template_url=None, parameters=None,
    notification_arns=None, disable_rollback=None, timeout_in_minutes=None,
    capabilities=None, tags=None, on_failure=None, stack_policy_body=None,
    stack_policy_url=None, region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        return conn.create_stack(name, template_body, template_url,
            parameters, notification_arns, disable_rollback,
            timeout_in_minutes, capabilities, tags, on_failure,
            stack_policy_body, stack_policy_url)
    except BotoServerError as e:
        msg = 'Failed to create stack {0}.\n{1}'.format(name, e)
        log.error(msg)
        log.debug(e)
        return False