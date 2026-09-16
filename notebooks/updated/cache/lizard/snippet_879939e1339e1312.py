def top(self, n=10, cache=None, prefetch=False):
    use_cache = self._use_cache(cache)
    if use_cache and len(self._top_cache) >= n:
        return self._top_cache[:n]
    soup = get(TOP).soup
    links = soup.find_all('a', class_='detLink')[:n]
    urls = [urlparse.urljoin(TOP, link.get('href')) for link in links]
    torrents = [self.torrent_from_url(url, use_cache, prefetch) for url in urls
        ]
    if use_cache:
        self._top_cache = torrents
        self._add_to_torrent_cache(torrents)
    return torrents