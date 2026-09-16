def page(self, order=values.unset, from_=values.unset, bounds=values.unset,
    page_token=values.unset, page_number=values.unset, page_size=values.unset):
    params = values.of({'Order': order, 'From': from_, 'Bounds': bounds,
        'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})
    response = self._version.page('GET', self._uri, params=params)
    return SyncListItemPage(self._version, response, self._solution)