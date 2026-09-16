def get_policy_definitions(settings):
    policy_definitions = {}
    for name in settings:
        if not name.startswith('multiauth.policy.'):
            continue
        value = settings[name]
        name = name[len('multiauth.policy.'):]
        policy_name, setting_name = name.split('.', 1)
        if policy_name not in policy_definitions:
            policy_definitions[policy_name] = {}
        policy_definitions[policy_name][setting_name] = value
    return policy_definitions