def exempt_urls(self):
    exempt_urls = list(self.get_settings('OIDC_EXEMPT_URLS', []))
    exempt_urls.extend(['oidc_authentication_init',
        'oidc_authentication_callback', 'oidc_logout'])
    return set([(url if url.startswith('/') else reverse(url)) for url in
        exempt_urls])