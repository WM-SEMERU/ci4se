def create_space(deployment_name, space_name, security_policy='public',
    events_retention_days=0, metrics_retention_days=0, token_manager=None,
    app_url=defaults.APP_URL):
    deployment_id = get_deployment_id(deployment_name, token_manager=
        token_manager, app_url=app_url)
    payload = {'name': space_name, 'security_policy': security_policy,
        'events_retention_days': events_retention_days,
        'metrics_retention_days': metrics_retention_days}
    headers = token_manager.get_access_token_headers()
    deployment_url = environment.get_deployment_url(app_url=app_url)
    response = requests.post('%s/api/v1/deployments/%s/spaces' % (
        deployment_url, deployment_id), data=json.dumps(payload), headers=
        headers)
    if response.status_code == 201:
        return response.json()
    else:
        raise JutException('Error %s: %s' % (response.status_code, response
            .text))