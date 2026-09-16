def _request_reports(self, domains):
    params = [{'url': domain} for domain in domains]
    responses = self._requests.multi_get(self.BASE_URL, query_params=params,
        to_json=False)
    return responses