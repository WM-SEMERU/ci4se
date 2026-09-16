def get_page(self, target_url):
    response = self._version.domain.twilio.request('GET', target_url)
    return SyncListPage(self._version, response, self._solution)