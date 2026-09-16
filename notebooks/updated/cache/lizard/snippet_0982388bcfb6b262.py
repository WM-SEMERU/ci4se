def get_action_cache(self, action_key):
    data = None
    if self.cache:
        data = self.cache.get(self.app.config['ACCESS_ACTION_CACHE_PREFIX'] +
            action_key)
    return data