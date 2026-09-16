def get_output_cache_key(self, placeholder_name, instance):
    cachekey = self.get_output_cache_base_key(placeholder_name, instance)
    if self.cache_output_per_site:
        cachekey = '{0}-s{1}'.format(cachekey, settings.SITE_ID)
    if self.cache_output_per_language:
        user_language = get_language()
        if user_language not in self.cache_supported_language_codes:
            user_language = 'unsupported'
        cachekey = '{0}.{1}'.format(cachekey, user_language)
    return cachekey