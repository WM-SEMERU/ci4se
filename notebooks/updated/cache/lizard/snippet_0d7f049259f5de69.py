def create_client_with_lazy_load(api_key, cache_time_to_live_seconds=60,
    config_cache_class=None, base_url=None):
    if api_key is None:
        raise ConfigCatClientException('API Key is required.')
    if cache_time_to_live_seconds < 1:
        cache_time_to_live_seconds = 1
    return ConfigCatClient(api_key, 0, 0, None, cache_time_to_live_seconds,
        config_cache_class, base_url)