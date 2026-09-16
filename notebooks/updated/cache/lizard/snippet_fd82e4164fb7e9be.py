def update_stack(name, template_body=None, template_url=None, parameters=
    None, notification_arns=None, disable_rollback=False,
    timeout_in_minutes=None, capabilities=None, tags=None,
    use_previous_template=None, stack_policy_during_update_body=None,
    stack_policy_during_update_url=None, stack_policy_body=None,
    stack_policy_url=None, region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        update = conn.update_stack(name, template_body, template_url,
            parameters, notification_arns, disable_rollback,
            timeout_in_minutes, capabilities, tags, use_previous_template,
            stack_policy_during_update_body, stack_policy_during_update_url,
            stack_policy_body, stack_policy_url)
        log.debug('Updated result is : %s.', update)
        return update
    except BotoServerError as e:
        msg = 'Failed to update stack {0}.'.format(name)
        log.debug(e)
        log.error(msg)
        return six.text_type(e)