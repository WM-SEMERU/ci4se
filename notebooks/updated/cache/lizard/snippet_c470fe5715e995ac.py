def make_session(scraper):
    cache_path = os.path.join(scraper.config.data_path, 'cache')
    cache_policy = scraper.config.cache_policy
    cache_policy = cache_policy.lower().strip()
    session = ScraperSession()
    session.scraper = scraper
    session.cache_policy = cache_policy
    adapter = CacheControlAdapter(FileCache(cache_path), cache_etags=True,
        controller_class=PolicyCacheController)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session