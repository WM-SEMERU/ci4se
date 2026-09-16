def api_related(self, query):
    url = '{0}/{1}/related/?format=json'.format(self.base_url, query)
    response = requests.get(url, headers=self.headers, verify=self.verify_ssl)
    if response.status_code == 200:
        return response.json()
    else:
        self.error(
            'Received status code: {0} from Soltra Server. Content:\n{1}'.
            format(response.status_code, response.text))