def request(self, method, resource, params=None):
    url = self.get_url(resource, params)
    headers = {'Content-Type': 'application/json'}
    auth = requests.auth.HTTPBasicAuth(self.username, self.password)
    log.info('Request to %s. Data: %s' % (url, params))
    response = requests.request(method, url, data=json.dumps(params),
        headers=headers, auth=auth)
    response.raise_for_status()
    log.info('Response from %s: %s' % (url, response.text))
    content = response.json()
    self.parse_status(content.get('status'))
    return content