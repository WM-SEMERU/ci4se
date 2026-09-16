def is_remote_allowed(remote):
    if settings.debug:
        return True
    if not remote:
        return False
    for domain_pattern in settings.node['cors_whitelist_domains']:
        if domain_pattern.match(remote):
            return True
    return False