def get_existing_pipelines(self):
    url = '{0}/applications/{1}/pipelineConfigs'.format(API_URL, self.app_name)
    resp = requests.get(url, verify=GATE_CA_BUNDLE, cert=GATE_CLIENT_CERT)
    assert resp.ok, 'Failed to lookup pipelines for {0}: {1}'.format(self.
        app_name, resp.text)
    return resp.json()