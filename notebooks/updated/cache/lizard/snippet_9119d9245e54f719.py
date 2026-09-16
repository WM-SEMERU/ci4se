def get_details(app='groupproject', env='dev', region='us-east-1'):
    url = '{host}/applications/{app}'.format(host=API_URL, app=app)
    request = requests.get(url, verify=GATE_CA_BUNDLE, cert=GATE_CLIENT_CERT)
    if not request.ok:
        raise SpinnakerAppNotFound('"{0}" not found.'.format(app))
    app_details = request.json()
    LOG.debug('App details: %s', app_details)
    group = app_details['attributes'].get('repoProjectKey')
    project = app_details['attributes'].get('repoSlug')
    generated = gogoutils.Generator(group, project, env=env, region=region,
        formats=APP_FORMATS)
    LOG.debug('Application details: %s', generated)
    return generated