def verify_deprecated_policy(old_policy, new_policy, default_rule, context):
    if _ENFORCER:
        current_rule = str(_ENFORCER.rules[old_policy])
    else:
        current_rule = None
    if current_rule != default_rule:
        LOG.warning(
            "Start using the new action '{0}'. The existing action '{1}' is being deprecated and will be removed in future release."
            .format(new_policy, old_policy))
        target = {'project_id': context.project_id, 'user_id': context.user_id}
        return authorize(context=context, action=old_policy, target=target)
    else:
        return False