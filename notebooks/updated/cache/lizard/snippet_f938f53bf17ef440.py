def get_whitelist_page(self, page_number=None, page_size=None):
    params = {'pageNumber': page_number, 'pageSize': page_size}
    resp = self._client.get('whitelist', params=params)
    return Page.from_dict(resp.json(), content_type=Indicator)