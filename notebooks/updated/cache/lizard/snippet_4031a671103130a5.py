def get_linked_cases(self, case_id):
    req = self.url + '/api/case/{}/links'.format(case_id)
    try:
        return requests.get(req, proxies=self.proxies, auth=self.auth,
            verify=self.cert)
    except requests.exceptions.RequestException as e:
        raise CaseException('Linked cases fetch error: {}'.format(e))