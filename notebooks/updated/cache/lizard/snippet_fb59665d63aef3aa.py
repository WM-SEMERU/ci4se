def login_with_token(refresh_token, team=None):
    _check_team_id(team)
    auth = _update_auth(team, refresh_token)
    url = get_registry_url(team)
    contents = _load_auth()
    contents[url] = auth
    _save_auth(contents)
    _clear_session(team)