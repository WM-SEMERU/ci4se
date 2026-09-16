def list_teams(profile='github', ignore_cache=False):
    key = 'github.{0}:teams'.format(_get_config_value(profile, 'org_name'))
    if key not in __context__ or ignore_cache:
        client = _get_client(profile)
        organization = client.get_organization(_get_config_value(profile,
            'org_name'))
        teams_data = organization.get_teams()
        teams = {}
        for team in teams_data:
            teams[team.name] = {'id': team.id, 'slug': team.slug,
                'description': team._rawData['description'], 'permission':
                team.permission, 'privacy': team._rawData['privacy']}
        __context__[key] = teams
    return __context__[key]