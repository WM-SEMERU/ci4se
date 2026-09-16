def page(self, page_token=values.unset, page_number=values.unset, page_size
    =values.unset):
    params = values.of({'PageToken': page_token, 'Page': page_number,
        'PageSize': page_size})
    response = self._version.page('GET', self._uri, params=params)
    return SyncListPage(self._version, response, self._solution)