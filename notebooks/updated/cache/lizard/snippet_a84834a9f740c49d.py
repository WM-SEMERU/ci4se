def clear_scroll(self, scroll_id=None, body='', params={}, callback=None,
    **kwargs):
    url = self.mk_url(*['_search', 'scroll', scroll_id])
    self.client.fetch(self.mk_req(url, method='DELETE', body=body, **kwargs
        ), callback=callback)