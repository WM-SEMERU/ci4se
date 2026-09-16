def get_html(self, url, params=None, cache_cb=None, **kwargs):
    url = add_params(url, params)
    cache_consumed, value = self.try_read_cache(url)
    if cache_consumed:
        html = value
    else:
        self._create_driver()
        self.driver.get(url)
        html = self.driver.page_source
    if self.should_we_update_cache(html, cache_cb, cache_consumed):
        self.cache.set(url, html, expire=kwargs.get('cache_expire', self.
            cache_expire))
    return html