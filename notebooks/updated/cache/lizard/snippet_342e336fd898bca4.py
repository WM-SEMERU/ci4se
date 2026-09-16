def list_team_members(team_name, profile='github', ignore_cache=False):
    cached_team = get_team(team_name, profile=profile)
    if not cached_team:
        log.error('Team %s does not exist.', team_name)
        return False
    if cached_team.get('members') and not ignore_cache:
        return cached_team.get('members')
    try:
        client = _get_client(profile)
        organization = client.get_organization(_get_config_value(profile,
            'org_name'))
        team = organization.get_team(cached_team['id'])
    except UnknownObjectException:
        log.exception('Resource not found: %s', cached_team['id'])
    try:
        cached_team['members'] = [member.login.lower() for member in team.
            get_members()]
        return cached_team['members']
    except UnknownObjectException:
        log.exception('Resource not found: %s', cached_team['id'])
        return []