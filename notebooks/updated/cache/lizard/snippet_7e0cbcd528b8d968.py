def get_users(profile='pagerduty', subdomain=None, api_key=None):
    return _list_items('users', 'id', profile=profile, subdomain=subdomain,
        api_key=api_key)