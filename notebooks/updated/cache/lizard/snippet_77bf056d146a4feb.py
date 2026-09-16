def get_all_pipelines(app=''):
    url = '{host}/applications/{app}/pipelineConfigs'.format(host=API_URL,
        app=app)
    response = requests.get(url, verify=GATE_CA_BUNDLE, cert=GATE_CLIENT_CERT)
    assert response.ok, 'Could not retrieve Pipelines for {0}.'.format(app)
    pipelines = response.json()
    LOG.debug('Pipelines:\n%s', pipelines)
    return pipelines