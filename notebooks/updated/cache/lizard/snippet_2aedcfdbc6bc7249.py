def profile_list(default_only=False):
    profiles = {}
    default_profiles = ['All']
    with salt.utils.files.fopen('/etc/security/policy.conf', 'r'
        ) as policy_conf:
        for policy in policy_conf:
            policy = salt.utils.stringutils.to_unicode(policy)
            policy = policy.split('=')
            if policy[0].strip() == 'PROFS_GRANTED':
                default_profiles.extend(policy[1].strip().split(','))
    with salt.utils.files.fopen('/etc/security/prof_attr', 'r') as prof_attr:
        for profile in prof_attr:
            profile = salt.utils.stringutils.to_unicode(profile)
            profile = profile.split(':')
            if len(profile) != 5:
                continue
            profiles[profile[0]] = profile[3]
    if default_only:
        for p in [p for p in profiles if p not in default_profiles]:
            del profiles[p]
    return profiles