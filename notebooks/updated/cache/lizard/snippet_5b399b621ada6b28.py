def _delete(url, profile):
    request_url = '{0}/api/dashboards/{1}'.format(profile.get('grafana_url'
        ), url)
    response = requests.delete(request_url, headers={'Accept':
        'application/json', 'Authorization': 'Bearer {0}'.format(profile.
        get('grafana_token'))}, timeout=profile.get('grafana_timeout'))
    data = response.json()
    return data