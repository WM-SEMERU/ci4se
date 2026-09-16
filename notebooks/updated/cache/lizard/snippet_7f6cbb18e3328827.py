def get_server_group(self):
    api_url = '{0}/applications/{1}'.format(API_URL, self.app)
    response = requests.get(api_url, verify=GATE_CA_BUNDLE, cert=
        GATE_CLIENT_CERT)
    for server_group in response.json()['clusters'][self.env]:
        return server_group['serverGroups'][-1]