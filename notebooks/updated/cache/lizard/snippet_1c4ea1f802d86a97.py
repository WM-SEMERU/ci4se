def next_batch(self):
    is_success, results = AtlasRequest(url_path=self.atlas_url, user_agent=
        self._user_agent, server=self.server, verify=self.verify).get()
    if not is_success:
        raise APIResponseError(results)
    self.total_count = results.get('count')
    self.atlas_url = self.build_next_url(results.get('next'))
    self.current_batch = results.get('results', [])